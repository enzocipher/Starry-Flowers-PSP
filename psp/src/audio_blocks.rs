//! Host-testable helpers for filling fixed-size audio blocks from a file.
//!
//! The PSP worker currently owns its I/O loop in `audio.rs`; this module keeps
//! the block/EOF policy independent of PSP APIs so it can be tested on a host.

/// Maximum read/seek errors tolerated while assembling one output block.
pub const MAX_IO_ERRORS_PER_BLOCK: usize = 3;

/// Outcome of attempting to fill a block. Any unused tail must remain zeroed.
#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub enum FillOutcome {
    /// The entire output block was filled.
    Full,
    /// A non-looping stream reached EOF. `bytes` may be zero or a partial block.
    EndOfFile { bytes: usize },
    /// A looping stream had no data to read, so retrying would spin forever.
    EmptyLoop { bytes: usize },
    /// I/O kept failing after the per-block retry limit.
    IoErrors { bytes: usize, errors: usize },
}

/// Fill `block`, preserving any existing prefix and leaving its unused tail
/// unchanged (callers should zero it before use). In looping mode, EOF seeks
/// to the beginning and continues filling; an empty stream ends immediately.
///
/// The error count is bounded for the entire block, so intermittent failures
/// cannot keep the audio worker in an unbounded retry loop.
pub fn fill_block<E>(
    block: &mut [u8],
    looping: bool,
    mut read: impl FnMut(&mut [u8]) -> Result<usize, E>,
    mut seek_to_start: impl FnMut() -> Result<(), E>,
) -> FillOutcome {
    let mut filled = 0;
    let mut errors = 0;
    let mut just_wrapped = false;

    while filled < block.len() {
        match read(&mut block[filled..]) {
            Ok(0) => {
                if !looping {
                    return FillOutcome::EndOfFile { bytes: filled };
                }
                if just_wrapped {
                    return FillOutcome::EmptyLoop { bytes: filled };
                }
                if let Err(_) = seek_to_start() {
                    errors += 1;
                    if errors >= MAX_IO_ERRORS_PER_BLOCK {
                        return FillOutcome::IoErrors {
                            bytes: filled,
                            errors,
                        };
                    }
                    continue;
                }
                just_wrapped = true;
            }
            Ok(count) if count <= block.len() - filled => {
                filled += count;
                just_wrapped = false;
            }
            Ok(_) | Err(_) => {
                errors += 1;
                if errors >= MAX_IO_ERRORS_PER_BLOCK {
                    return FillOutcome::IoErrors {
                        bytes: filled,
                        errors,
                    };
                }
            }
        }
    }

    FillOutcome::Full
}

#[cfg(test)]
mod tests {
    use super::{fill_block, FillOutcome, MAX_IO_ERRORS_PER_BLOCK};
    use std::collections::VecDeque;
    use std::{
        cell::RefCell,
        io::{Cursor, Read, Seek, SeekFrom},
    };

    #[test]
    fn looping_eof_completes_a_partial_block_from_the_start() {
        let mut block = [0; 4];
        let source = RefCell::new(Cursor::new(vec![1, 2, 3]));
        let outcome = fill_block(
            &mut block,
            true,
            |out| source.borrow_mut().read(out).map_err(|_| ()),
            || {
                source
                    .borrow_mut()
                    .seek(SeekFrom::Start(0))
                    .map(|_| ())
                    .map_err(|_| ())
            },
        );
        assert_eq!(outcome, FillOutcome::Full);
        assert_eq!(block, [1, 2, 3, 1]);
    }

    #[test]
    fn short_looping_track_repeats_as_many_times_as_needed() {
        let mut block = [0; 5];
        let source = RefCell::new(Cursor::new(vec![9]));
        let outcome = fill_block(
            &mut block,
            true,
            |out| source.borrow_mut().read(out).map_err(|_| ()),
            || {
                source
                    .borrow_mut()
                    .seek(SeekFrom::Start(0))
                    .map(|_| ())
                    .map_err(|_| ())
            },
        );
        assert_eq!(outcome, FillOutcome::Full);
        assert_eq!(block, [9; 5]);
    }

    #[test]
    fn empty_looping_stream_terminates_without_retrying_forever() {
        let mut block = [0; 4];
        let mut seeks = 0;
        let outcome = fill_block(
            &mut block,
            true,
            |_| Ok::<_, ()>(0),
            || {
                seeks += 1;
                Ok::<_, ()>(())
            },
        );
        assert_eq!(outcome, FillOutcome::EmptyLoop { bytes: 0 });
        assert_eq!(seeks, 1);
    }

    #[test]
    fn non_looping_partial_eof_keeps_partial_count_and_zero_tail() {
        let mut block = [0; 4];
        let mut chunks = VecDeque::from([vec![7, 8], vec![]]);
        let outcome = fill_block(
            &mut block,
            false,
            |out| {
                let data = chunks.pop_front().unwrap();
                out[..data.len()].copy_from_slice(&data);
                Ok::<_, ()>(data.len())
            },
            || Ok::<_, ()>(()),
        );
        assert_eq!(outcome, FillOutcome::EndOfFile { bytes: 2 });
        assert_eq!(block, [7, 8, 0, 0]);
    }

    #[test]
    fn repeated_io_errors_are_bounded_for_one_block() {
        let mut block = [0; 4];
        let mut attempts = 0;
        let outcome = fill_block(
            &mut block,
            true,
            |_| {
                attempts += 1;
                Err::<usize, _>(())
            },
            || Ok::<_, ()>(()),
        );
        assert_eq!(
            outcome,
            FillOutcome::IoErrors {
                bytes: 0,
                errors: MAX_IO_ERRORS_PER_BLOCK
            }
        );
        assert_eq!(attempts, MAX_IO_ERRORS_PER_BLOCK);
    }

    #[test]
    fn transient_read_error_recovers_and_fills_the_block() {
        let mut block = [0; 2];
        let mut attempts = 0;
        let outcome = fill_block(
            &mut block,
            false,
            |out| {
                attempts += 1;
                if attempts == 1 {
                    return Err(());
                }
                out.copy_from_slice(&[3, 4]);
                Ok::<_, ()>(2)
            },
            || Ok::<_, ()>(()),
        );
        assert_eq!(outcome, FillOutcome::Full);
        assert_eq!(block, [3, 4]);
    }

    #[test]
    fn repeated_seek_errors_stop_after_the_retry_limit() {
        let mut block = [0; 2];
        let mut reads = 0;
        let mut seeks = 0;
        let outcome = fill_block(
            &mut block,
            true,
            |_| {
                reads += 1;
                if reads == 1 {
                    Ok::<_, ()>(1)
                } else {
                    Ok(0)
                }
            },
            || {
                seeks += 1;
                Err::<(), _>(())
            },
        );
        assert_eq!(
            outcome,
            FillOutcome::IoErrors {
                bytes: 1,
                errors: MAX_IO_ERRORS_PER_BLOCK
            }
        );
        assert_eq!(seeks, MAX_IO_ERRORS_PER_BLOCK);
    }
}
