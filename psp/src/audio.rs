//! Native blocking audio workers; no allocation or spin locks on audio threads.
use crate::audio_blocks::{self, FillOutcome};
use alloc::{collections::BTreeMap, format, string::String, sync::Arc, vec::Vec};
use core::{
    ffi::c_void,
    ptr,
    sync::atomic::{AtomicI32, AtomicU32, Ordering},
};
use psp::sys;

const BLOCK_BYTES: usize = 4096;
const BLOCK_SAMPLES: usize = BLOCK_BYTES / core::mem::size_of::<i16>();
const MAX_OUTPUT_ERRORS: u8 = 3;
const RETRY_DELAY_US: i64 = 500_000;

struct Shared {
    paths: Vec<Vec<u8>>,
    names: Vec<String>,
    looping: bool,
    selected: AtomicU32,
    generation: AtomicU32,
    volume: AtomicI32,
    status: AtomicI32,
    blocks: AtomicU32,
}
pub struct Audio {
    shared: Arc<Shared>,
}
impl Audio {
    pub fn new(root: &str, files: &BTreeMap<String, String>, looping: bool) -> Self {
        let names: Vec<_> = files.values().cloned().collect();
        let paths = names
            .iter()
            .map(|name| {
                let mut path = format!("{root}/DATA/{name}").into_bytes();
                path.push(0);
                path
            })
            .collect();
        let shared = Arc::new(Shared {
            paths,
            names,
            looping,
            selected: AtomicU32::new(u32::MAX),
            generation: AtomicU32::new(0),
            volume: AtomicI32::new(32768),
            status: AtomicI32::new(-1),
            blocks: AtomicU32::new(0),
        });
        unsafe {
            let thread = sys::sceKernelCreateThread(
                b"StarryAudio\0".as_ptr(),
                worker,
                0x18,
                16 * 1024,
                sys::ThreadAttributes::USER,
                ptr::null_mut(),
            );
            if thread.0 > 0 {
                let mut arg = Arc::into_raw(shared.clone());
                let result = sys::sceKernelStartThread(
                    thread,
                    core::mem::size_of_val(&arg),
                    (&mut arg as *mut *const Shared).cast(),
                );
                if result < 0 {
                    drop(Arc::from_raw(arg));
                    shared.status.store(result, Ordering::Relaxed);
                }
            } else {
                shared.status.store(thread.0, Ordering::Relaxed);
            }
        }
        Self { shared }
    }
    pub fn update(&self, filename: &str, volume: f32, restart: bool) {
        self.shared
            .volume
            .store((volume.clamp(0., 1.) * 32768.) as i32, Ordering::Relaxed);
        // An empty sound event changes volume without cutting the previous sound short.
        if filename.is_empty() && !self.shared.looping {
            return;
        }
        let selected = self
            .shared
            .names
            .iter()
            .position(|s| s == filename)
            .map(|i| i as u32)
            .unwrap_or(u32::MAX);
        if restart || selected != self.shared.selected.load(Ordering::Relaxed) {
            self.shared.selected.store(selected, Ordering::Relaxed);
            self.shared.generation.fetch_add(1, Ordering::Release);
        }
    }
    pub fn blocks(&self) -> u32 {
        self.shared.blocks.load(Ordering::Relaxed)
    }
}
unsafe extern "C" fn worker(_: usize, arg: *mut c_void) -> i32 {
    let shared = Arc::from_raw(*(arg as *const *const Shared));
    let mut channel = -1;
    let mut channel_retry_at = 0;
    let mut fd = sys::SceUid(-1);
    let mut generation = u32::MAX;
    let mut samples = [0i16; BLOCK_SAMPLES];
    let mut output_errors = 0u8;
    let mut retry_open = false;
    let mut file_retry_at = 0;
    loop {
        let time = sys::sceKernelGetSystemTimeWide();
        if channel < 0 {
            if time < channel_retry_at {
                sys::sceKernelDelayThread(10_000);
                continue;
            }
            channel = sys::sceAudioChReserve(-1, 1024, sys::AudioFormat::Stereo);
            shared.status.store(channel, Ordering::Relaxed);
            if channel < 0 {
                channel_retry_at = time + RETRY_DELAY_US;
                sys::sceKernelDelayThread(10_000);
                continue;
            }
        }
        let next = shared.generation.load(Ordering::Acquire);
        if next != generation || retry_open && time >= file_retry_at {
            generation = next;
            output_errors = 0;
            if fd.0 >= 0 {
                sys::sceIoClose(fd);
            }
            let selected = shared.selected.load(Ordering::Relaxed) as usize;
            fd = shared
                .paths
                .get(selected)
                .map(|p| sys::sceIoOpen(p.as_ptr(), sys::IoOpenFlags::RD_ONLY, 0))
                .unwrap_or(sys::SceUid(-1));
            retry_open = shared.looping && fd.0 < 0 && selected < shared.paths.len();
            file_retry_at = time + RETRY_DELAY_US;
        }
        if fd.0 < 0 {
            sys::sceKernelDelayThread(10_000);
            continue;
        }
        samples.fill(0);
        let outcome = audio_blocks::fill_block(
            unsafe {
                core::slice::from_raw_parts_mut(samples.as_mut_ptr().cast::<u8>(), BLOCK_BYTES)
            },
            shared.looping,
            |buffer| {
                let n =
                    unsafe { sys::sceIoRead(fd, buffer.as_mut_ptr().cast(), buffer.len() as u32) };
                if n >= 0 {
                    Ok(n as usize)
                } else {
                    Err(())
                }
            },
            || {
                if sys::sceIoLseek(fd, 0, sys::IoWhence::Set) >= 0 {
                    Ok(())
                } else {
                    Err(())
                }
            },
        );
        let n = match outcome {
            FillOutcome::Full => BLOCK_BYTES,
            FillOutcome::EndOfFile { bytes } => bytes,
            FillOutcome::EmptyLoop { bytes } => bytes,
            FillOutcome::IoErrors { bytes, .. } => bytes,
        };
        // Only music retries failed I/O. A completed effect or an empty loop
        // must stay stopped until the next selection, rather than replaying.
        if shared.looping && matches!(outcome, FillOutcome::IoErrors { .. }) {
            retry_open = true;
            file_retry_at = time + RETRY_DELAY_US;
        }
        if n == 0 {
            // Close EOF/error sources; any music retry waits for its deadline.
            sys::sceIoClose(fd);
            fd = sys::SceUid(-1);
            sys::sceKernelDelayThread(10_000);
            continue;
        }
        if matches!(
            outcome,
            FillOutcome::EmptyLoop { .. } | FillOutcome::IoErrors { .. }
        ) {
            sys::sceIoClose(fd);
            fd = sys::SceUid(-1);
        }
        // The helper leaves the tail untouched for non-looping partial blocks.
        // Clear it explicitly so playback never emits stale samples.
        if n < BLOCK_BYTES {
            unsafe {
                core::ptr::write_bytes(
                    (samples.as_mut_ptr().cast::<u8>()).add(n),
                    0,
                    BLOCK_BYTES - n,
                );
            }
        }
        let result = sys::sceAudioOutputBlocking(
            channel,
            shared.volume.load(Ordering::Relaxed),
            samples.as_mut_ptr().cast(),
        );
        if result >= 0 {
            shared.blocks.fetch_add(1, Ordering::Relaxed);
            output_errors = 0;
        } else {
            output_errors = output_errors.saturating_add(1);
            sys::sceKernelDelayThread(10_000);
        }
        if output_errors >= MAX_OUTPUT_ERRORS {
            shared.status.store(result, Ordering::Relaxed);
            sys::sceAudioChRelease(channel);
            channel = -1;
            channel_retry_at = sys::sceKernelGetSystemTimeWide() + RETRY_DELAY_US;
            output_errors = 0;
        }
    }
}
