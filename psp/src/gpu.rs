//! GPU sprites retain source texture resolution, including in PPSSPP.
//! Draw source-resolution DXT5 art directly; RAM snapshots are only for dissolves.
//! Sampling persistent VRAM aliases caused corrupted menus in PPSSPP.
//! Cached surfaces use RGB sampling because framebuffer alpha stores stencil.
//! Finish the GE list before evicting textures or reusing list memory.
use alloc::{collections::BTreeMap, sync::Arc, vec, vec::Vec};
use core::{ffi::c_void, ptr};
use psp::sys::*;
#[repr(C, align(16))]
#[derive(Clone)]
struct Block([u8; 16]);
#[derive(Clone)]
pub struct Draw {
    pub file: Arc<str>,
    pub tw: usize,
    pub th: usize,
    pub font: bool,
    pub dxt5: bool,
    pub xy: [f32; 4],
    pub uv: [f32; 4],
    pub color: u32,
}
#[derive(Clone)]
pub struct Frame {
    pub clear: u32,
    pub draws: Vec<Draw>,
    pub scene_len: usize,
    pub prefix_len: usize,
    pub prefix_sealed: bool,
    pub fade_alpha: u32,
    pub offset: [f32; 2],
    pub origin: Option<u64>,
    pub fade_source: Option<u64>,
}
impl Frame {
    pub fn new() -> Self {
        Self {
            clear: 0xff000000,
            draws: Vec::new(),
            scene_len: 0,
            prefix_len: 0,
            prefix_sealed: false,
            fade_alpha: 255,
            offset: [0., 0.],
            origin: None,
            fade_source: None,
        }
    }
    pub fn fill(&mut self, c: u32) {
        self.clear = c;
        self.draws.clear();
        self.fade_alpha = 255;
        self.offset = [0., 0.];
        self.scene_len = 0;
        self.prefix_len = 0;
        self.prefix_sealed = false;
        self.origin = None;
        self.fade_source = None;
    }
    pub fn fade_from(&mut self, old: &Self, alpha: u32) {
        // Fade cached complete scenes; never decompress both scenes every frame.
        self.fade_alpha = alpha.min(255);
        self.fade_source = old.origin;
    }
    pub fn offset(&mut self, x: i32, y: i32) {
        self.offset = [x as f32, y as f32];
    }
    pub fn signature(&self, len: usize) -> u64 {
        let mut key = self.clear as u64;
        for d in &self.draws[..len] {
            for b in d
                .file
                .bytes()
                .chain([0])
                .chain(d.tw.to_le_bytes())
                .chain(d.th.to_le_bytes())
                .chain([d.font as u8, d.dxt5 as u8])
                .chain(d.xy.iter().flat_map(|v| v.to_bits().to_le_bytes()))
                .chain(d.uv.iter().flat_map(|v| v.to_bits().to_le_bytes()))
                .chain(d.color.to_le_bytes())
            {
                key = (key ^ b as u64).wrapping_mul(1099511628211);
            }
        }
        key
    }
}
struct Cached {
    data: Vec<Block>,
    used: u64,
}
pub struct Gpu {
    list: Vec<Block>,
    palette: Vec<Block>,
    cache: BTreeMap<Arc<str>, Cached>,
    clock: u64,
    queued: usize,
    scene_key: u64,
    scene_origin: Option<u64>,
    old_origin: Option<u64>,
    scene_pixels: Vec<Block>,
    old_pixels: Vec<Block>,
    prefix_pixels: Vec<Block>,
    prefix_key: u64,
    pub prefix_renders: usize,
    old_valid: bool,
    pub texture_loads: usize,
    pub scene_renders: usize,
    pub load_ms: f64,
    pub inflate_ms: f64,
    cache_bytes: usize,
    retained_scene: Frame,
    retained_key: u64,
}
#[repr(C)]
struct Vertex {
    u: f32,
    v: f32,
    color: u32,
    x: f32,
    y: f32,
    z: f32,
}
impl Gpu {
    pub fn new() -> Self {
        let mut palette = vec![Block([0; 16]); 64];
        for i in 0..256 {
            palette[i / 4].0[(i % 4) * 4..(i % 4 + 1) * 4]
                .copy_from_slice(&((i as u32) << 24 | 0xffffff).to_le_bytes());
        }
        let mut s = Self {
            list: vec![Block([0; 16]); 16384],
            palette,
            cache: BTreeMap::new(),
            clock: 0,
            queued: 0,
            scene_key: 0,
            scene_origin: None,
            old_origin: None,
            scene_pixels: vec![Block([0; 16]); 512 * 512 / 4],
            old_pixels: vec![Block([0; 16]); 512 * 512 / 4],
            prefix_pixels: vec![Block([0; 16]); 512 * 512 / 4],
            prefix_key: 0,
            prefix_renders: 0,
            old_valid: false,
            texture_loads: 0,
            scene_renders: 0,
            load_ms: 0.,
            inflate_ms: 0.,
            cache_bytes: 0,
            retained_scene: Frame::new(),
            retained_key: 0,
        };
        unsafe {
            sceGuInit();
            sceKernelDcacheWritebackAll();
            s.start(0);
            sceGuDrawBuffer(DisplayPixelFormat::Psm8888, ptr::null_mut(), 512);
            sceGuDispBuffer(480, 272, ptr::null_mut(), 512);
            sceGuOffset(2048 - 240, 2048 - 136);
            sceGuViewport(2048, 2048, 480, 272);
            sceGuScissor(0, 0, 480, 272);
            sceGuEnable(GuState::ScissorTest);
            sceGuDisable(GuState::DepthTest);
            sceGuDisable(GuState::CullFace);
            sceGuDisable(GuState::Dither);
            sceGuEnable(GuState::Blend);
            sceGuBlendFunc(
                BlendOp::Add,
                BlendFactor::SrcAlpha,
                BlendFactor::OneMinusSrcAlpha,
                0,
                0,
            );
            sceGuTexFunc(TextureEffect::Modulate, TextureColorComponent::Rgba);
            sceGuTexWrap(GuTexWrapMode::Clamp, GuTexWrapMode::Clamp);
            sceGuTexScale(1., 1.);
            sceGuTexOffset(0., 0.);
            s.finish();
            sceGuDisplay(true);
        }
        s
    }
    unsafe fn start(&mut self, buffer: usize) {
        sceGuStart(GuContextType::Direct, self.list.as_mut_ptr().cast());
        sceGuDrawBufferList(
            DisplayPixelFormat::Psm8888,
            (buffer * 512 * 272 * 4) as *mut c_void,
            512,
        );
        self.queued = 0;
    }
    unsafe fn finish(&mut self) {
        sceGuFinish();
        sceGuSync(GuSyncMode::Finish, GuSyncBehavior::Wait);
    }
    pub fn present(&mut self, frame: &Frame, root: &str, buffer: usize) {
        let current_key = frame.signature(frame.scene_len);
        let fading = frame.fade_alpha < 255
            && frame.fade_source.is_some()
            && ((self.old_valid
                && self.scene_key == current_key
                && self.old_origin == frame.fade_source)
                || (self.retained_scene.origin == frame.fade_source
                    && self.retained_key != current_key));
        if fading && self.scene_key == 0 {
            // Capture the real preceding scene only when a dissolve needs it.
            let source = core::mem::replace(&mut self.retained_scene, Frame::new());
            self.draw(&source, root, 2);
            unsafe {
                self.start(2);
                sceGuCopyImage(
                    DisplayPixelFormat::Psm8888,
                    0,
                    0,
                    480,
                    272,
                    512,
                    0x04110000usize as *mut c_void,
                    0,
                    0,
                    512,
                    self.scene_pixels.as_mut_ptr().cast(),
                );
                self.finish();
                sceKernelDcacheInvalidateRange(
                    self.scene_pixels.as_mut_ptr().cast(),
                    512 * 272 * 4,
                );
            }
            self.scene_key = self.retained_key;
            self.scene_origin = source.origin;
            self.retained_scene = source;
        }
        if !fading {
            // Draw source textures directly: a RAM screenshot would destroy emulator scaling detail.
            self.scene_key = 0;
            self.old_valid = false;
            self.old_origin = None;
            self.scene_origin = frame.origin;
            self.draw_parts(
                frame.clear,
                &frame.draws[..frame.scene_len],
                &frame.draws[frame.scene_len..],
                root,
                buffer,
                frame.offset,
            );
        } else if frame.scene_len > 0 || frame.origin.is_some() {
            let key = frame.signature(frame.scene_len);
            if key != self.scene_key {
                self.old_valid = self.scene_key != 0;
                self.old_origin = self.scene_origin;
                core::mem::swap(&mut self.scene_pixels, &mut self.old_pixels);
                let mut scene = Frame::new();
                scene.clear = frame.clear;
                if frame.prefix_len > 0 {
                    let prefix_key = frame.signature(frame.prefix_len);
                    if prefix_key != self.prefix_key {
                        let mut prefix = Frame::new();
                        prefix.clear = frame.clear;
                        prefix.draws = frame.draws[..frame.prefix_len].to_vec();
                        // Buffer 2 is scratch; buffers 0/1 belong exclusively to display.
                        self.draw(&prefix, root, 2);
                        unsafe {
                            self.start(2);
                            sceGuCopyImage(
                                DisplayPixelFormat::Psm8888,
                                0,
                                0,
                                480,
                                272,
                                512,
                                0x04110000usize as *mut c_void,
                                0,
                                0,
                                512,
                                self.prefix_pixels.as_mut_ptr().cast(),
                            );
                            self.finish();
                            sceKernelDcacheInvalidateRange(
                                self.prefix_pixels.as_mut_ptr().cast(),
                                512 * 272 * 4,
                            );
                        }
                        self.prefix_key = prefix_key;
                        self.prefix_renders += 1;
                    }
                    scene.draws.push(Draw {
                        file: "@prefix".into(),
                        tw: 512,
                        th: 512,
                        font: false,
                        dxt5: false,
                        xy: [0., 0., 480., 272.],
                        uv: [0., 0., 480., 272.],
                        color: 0xffffffff,
                    });
                    scene
                        .draws
                        .extend_from_slice(&frame.draws[frame.prefix_len..frame.scene_len]);
                } else {
                    scene.draws = frame.draws[..frame.scene_len].to_vec();
                }
                self.draw(&scene, root, 2);
                unsafe {
                    self.start(2);
                    sceGuCopyImage(
                        DisplayPixelFormat::Psm8888,
                        0,
                        0,
                        480,
                        272,
                        512,
                        0x04110000usize as *mut c_void,
                        0,
                        0,
                        512,
                        self.scene_pixels.as_mut_ptr().cast(),
                    );
                    self.finish();
                    sceKernelDcacheInvalidateRange(
                        self.scene_pixels.as_mut_ptr().cast(),
                        512 * 272 * 4,
                    );
                }
                self.scene_key = key;
                self.scene_renders += 1;
            }
            // A new dialogue can reuse identical pixels; its provenance still advances.
            self.scene_origin = frame.origin;
            let fade_valid = self.old_valid
                && frame.fade_source.is_some()
                && frame.fade_source == self.old_origin;
            let surfaces = [
                Draw {
                    file: "@old".into(),
                    tw: 512,
                    th: 512,
                    font: false,
                    dxt5: false,
                    xy: [0., 0., 480., 272.],
                    uv: [0., 0., 480., 272.],
                    color: 0xffffffff,
                },
                Draw {
                    file: "@scene".into(),
                    tw: 512,
                    th: 512,
                    font: false,
                    dxt5: false,
                    xy: [
                        frame.offset[0],
                        frame.offset[1],
                        480. + frame.offset[0],
                        272. + frame.offset[1],
                    ],
                    uv: [0., 0., 480., 272.],
                    color: (if fade_valid { frame.fade_alpha } else { 255 }) << 24 | 0xffffff,
                },
            ];
            let first = if frame.fade_alpha < 255 && fade_valid {
                0
            } else {
                1
            };
            // Borrow overlays directly instead of cloning every glyph and filename each frame.
            self.draw_parts(
                frame.clear,
                &surfaces[first..],
                &frame.draws[frame.scene_len..],
                root,
                buffer,
                [0., 0.],
            );
        } else {
            self.scene_key = 0;
            self.scene_origin = None;
            self.old_origin = None;
            self.old_valid = false;
            self.draw(frame, root, buffer);
        }
        if self.retained_key != current_key {
            self.retained_scene.fill(frame.clear);
            self.retained_scene
                .draws
                .extend_from_slice(&frame.draws[..frame.scene_len]);
            self.retained_key = current_key;
        }
        self.retained_scene.origin = frame.origin;
        unsafe {
            sceDisplayWaitVblankStart();
            sceDisplaySetFrameBuf(
                (0x44000000usize + buffer * 512 * 272 * 4) as *const u8,
                512,
                DisplayPixelFormat::Psm8888,
                DisplaySetBufSync::Immediate,
            );
        }
    }
    fn draw(&mut self, frame: &Frame, root: &str, buffer: usize) {
        self.draw_parts(frame.clear, &frame.draws, &[], root, buffer, [0., 0.]);
    }
    fn draw_parts(
        &mut self,
        clear: u32,
        surfaces: &[Draw],
        overlays: &[Draw],
        root: &str,
        buffer: usize,
        offset: [f32; 2],
    ) {
        unsafe {
            self.start(buffer);
            sceGuClearColor(clear);
            sceGuClear(ClearBuffer::COLOR_BUFFER_BIT | ClearBuffer::FAST_CLEAR_BIT);
            let mut bound: Option<Arc<str>> = None;
            for (d, shift) in surfaces
                .iter()
                .map(|d| (d, offset))
                .chain(overlays.iter().map(|d| (d, [0., 0.])))
            {
                if self.queued > 400 {
                    self.finish();
                    self.start(buffer);
                    bound = None;
                }
                if bound.as_deref() != Some(d.file.as_ref()) || d.file.is_empty() {
                    if d.file.starts_with("@") {
                        sceGuTexFunc(TextureEffect::Modulate, TextureColorComponent::Rgb);
                        sceGuEnable(GuState::Texture2D);
                        sceGuTexMode(TexturePixelFormat::Psm8888, 0, 0, 0);
                        sceGuTexImage(
                            MipmapLevel::None,
                            512,
                            d.th as i32,
                            512,
                            if d.file.as_ref() == "@prefix" {
                                self.prefix_pixels.as_ptr().cast()
                            } else if d.file.as_ref() == "@old" {
                                self.old_pixels.as_ptr().cast()
                            } else {
                                self.scene_pixels.as_ptr().cast()
                            },
                        );
                        sceGuTexFilter(TextureFilter::Linear, TextureFilter::Linear);
                        sceGuTexFlush();
                    } else if !d.file.is_empty() {
                        sceGuTexFunc(TextureEffect::Modulate, TextureColorComponent::Rgba);
                        if !self.cache.contains_key(&d.file) {
                            self.finish();
                            let required = if d.font {
                                d.tw * d.th
                            } else if d.dxt5 {
                                d.tw * d.th * 21 / 16
                            } else {
                                d.tw * d.th * 4 * 21 / 16
                            };
                            while self.cache_bytes + (required + 15) / 16 * 16 > 6 * 1024 * 1024 {
                                let key = self
                                    .cache
                                    .iter()
                                    .filter(|(k, _)| {
                                        !matches!(
                                            k.as_ref(),
                                            "F08P00.RAW"
                                                | "F10P00.RAW"
                                                | "F12P00.RAW"
                                                | "F14P00.RAW"
                                                | "F18P00.RAW"
                                        )
                                    })
                                    .min_by_key(|(_, v)| v.used)
                                    .map(|(k, _)| k.clone())
                                    .unwrap();
                                if let Some(removed) = self.cache.remove(&key) {
                                    self.cache_bytes -= removed.data.len() * 16;
                                }
                            }
                            self.texture_loads += 1;
                            let load_started = crate::now();
                            if let Ok(mut file) =
                                crate::io::File::open(&alloc::format!("{root}/DATA/{}", d.file))
                            {
                                // Read directly into aligned texture memory: no inflate or second full copy.
                                let mut data = vec![Block([0; 16]); (required + 15) / 16];
                                let bytes = core::slice::from_raw_parts_mut(
                                    data.as_mut_ptr().cast::<u8>(),
                                    required,
                                );
                                let mut done = 0;
                                while done < required {
                                    let n =
                                        file.read(&mut bytes[done..]).expect("Texture read failed");
                                    assert!(n > 0, "Truncated texture");
                                    done += n;
                                }
                                self.load_ms += (crate::now() - load_started) * 1000.;
                                sceKernelDcacheWritebackRange(
                                    data.as_ptr().cast(),
                                    (data.len() * 16) as u32,
                                );
                                self.cache_bytes += data.len() * 16;
                                self.cache.insert(
                                    d.file.clone(),
                                    Cached {
                                        data,
                                        used: self.clock,
                                    },
                                );
                            }
                            self.start(buffer);
                        }
                        let Some(c) = self.cache.get_mut(&d.file) else {
                            continue;
                        };
                        self.clock += 1;
                        c.used = self.clock;
                        let data = c.data.as_ptr().cast::<u8>();
                        sceGuEnable(GuState::Texture2D);
                        if d.font {
                            sceGuTexMode(TexturePixelFormat::PsmT8, 0, 0, 0);
                            sceGuClutMode(ClutPixelFormat::Psm8888, 0, 255, 0);
                            sceGuClutLoad(32, self.palette.as_ptr().cast());
                            sceGuTexImage(
                                MipmapLevel::None,
                                d.tw as i32,
                                d.th as i32,
                                d.tw as i32,
                                data.cast(),
                            );
                            sceGuTexFilter(TextureFilter::Linear, TextureFilter::Linear);
                        } else {
                            sceGuTexMode(
                                if d.dxt5 {
                                    TexturePixelFormat::PsmDxt5
                                } else {
                                    TexturePixelFormat::Psm8888
                                },
                                2,
                                0,
                                0,
                            );
                            let mut offset = 0;
                            for (l, level) in
                                [MipmapLevel::None, MipmapLevel::Level1, MipmapLevel::Level2]
                                    .into_iter()
                                    .enumerate()
                            {
                                let w = d.tw >> l;
                                let h = d.th >> l;
                                sceGuTexImage(
                                    level,
                                    w as i32,
                                    h as i32,
                                    w as i32,
                                    data.add(offset).cast(),
                                );
                                offset += w * h * if d.dxt5 { 1 } else { 4 };
                            }
                            sceGuTexLevelMode(TextureLevelMode::Auto, 0.);
                            sceGuTexFilter(
                                TextureFilter::LinearMipmapLinear,
                                TextureFilter::Linear,
                            );
                        }
                        sceGuTexFlush();
                    } else {
                        sceGuDisable(GuState::Texture2D);
                    }
                    bound = Some(d.file.clone());
                } else if let Some(c) = self.cache.get_mut(&d.file) {
                    self.clock += 1;
                    c.used = self.clock;
                }
                let vertices =
                    sceGuGetMemory((core::mem::size_of::<Vertex>() * 2) as i32) as *mut Vertex;
                vertices.write(Vertex {
                    u: d.uv[0],
                    v: d.uv[1],
                    color: d.color,
                    x: d.xy[0] + shift[0],
                    y: d.xy[1] + shift[1],
                    z: 0.,
                });
                vertices.add(1).write(Vertex {
                    u: d.uv[2],
                    v: d.uv[3],
                    color: d.color,
                    x: d.xy[2] + shift[0],
                    y: d.xy[3] + shift[1],
                    z: 0.,
                });
                sceGuDrawArray(
                    GuPrimitive::Sprites,
                    VertexType::TEXTURE_32BITF
                        | VertexType::COLOR_8888
                        | VertexType::VERTEX_32BITF
                        | VertexType::TRANSFORM_2D,
                    2,
                    ptr::null(),
                    vertices.cast(),
                );
                self.queued += 1;
            }
            self.finish();
        }
    }
    pub fn pixels(&mut self, buffer: usize) -> Vec<u32> {
        // GE transfers require 16-byte alignment; Vec<u32> only guarantees four.
        let mut pixels = vec![Block([0; 16]); 480 * 272 / 4];
        unsafe {
            sceKernelDcacheWritebackAll();
            self.start(buffer);
            sceGuCopyImage(
                DisplayPixelFormat::Psm8888,
                0,
                0,
                480,
                272,
                512,
                (0x04000000usize + buffer * 512 * 272 * 4) as *mut c_void,
                0,
                0,
                480,
                pixels.as_mut_ptr().cast(),
            );
            self.finish();
            sceKernelDcacheInvalidateRange(pixels.as_mut_ptr().cast(), 480 * 272 * 4);
        }
        unsafe { core::slice::from_raw_parts(pixels.as_ptr().cast::<u32>(), 480 * 272).to_vec() }
    }
}
