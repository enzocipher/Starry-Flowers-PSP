//! Bounded GU bookkeeping and debug rasterization, also tested on the host.
use core::{convert::TryFrom, ptr::NonNull};

pub(crate) struct ObjectStack {
    entries: [Option<NonNull<u32>>; 32],
    depth: usize,
}

impl ObjectStack {
    pub const fn new() -> Self {
        Self {
            entries: [None; 32],
            depth: 0,
        }
    }

    pub fn is_empty(&self) -> bool {
        self.depth == 0
    }
    pub fn is_full(&self) -> bool {
        self.depth == self.entries.len()
    }

    pub fn push(&mut self, pointer: NonNull<u32>) -> bool {
        if self.is_full() {
            return false;
        }
        self.entries[self.depth] = Some(pointer);
        self.depth += 1;
        true
    }

    pub fn pop(&mut self) -> Option<NonNull<u32>> {
        if self.depth == 0 {
            return None;
        }
        self.depth -= 1;
        self.entries[self.depth].take()
    }
}

pub(crate) struct DebugSurface {
    pub offset: usize,
    pub stride: usize,
    pub width: usize,
    pub height: usize,
    pub bytes_per_pixel: usize,
}

impl DebugSurface {
    pub fn draw_glyph(&self, buffer: &mut [u8], x: i32, y: i32, color: u32, glyph: &[u8]) {
        let (Ok(x), Ok(y)) = (usize::try_from(x), usize::try_from(y)) else {
            return;
        };
        if glyph.len() != 8 || !matches!(self.bytes_per_pixel, 2 | 4) {
            return;
        }
        let Some(right) = x.checked_add(8) else {
            return;
        };
        let Some(bottom) = y.checked_add(8) else {
            return;
        };
        if right > self.width || right > self.stride || bottom > self.height {
            return;
        }
        // Validate the whole glyph before changing any pixel, including overflow.
        let end = (bottom - 1)
            .checked_mul(self.stride)
            .and_then(|p| p.checked_add(right))
            .and_then(|p| p.checked_mul(self.bytes_per_pixel))
            .and_then(|p| p.checked_add(self.offset));
        if !end.is_some_and(|end| end <= buffer.len()) {
            return;
        }
        let bytes = color.to_le_bytes();
        for (row, bits) in glyph.iter().enumerate() {
            for column in 0..8 {
                if bits & (1 << column) != 0 {
                    let offset =
                        self.offset + ((y + row) * self.stride + x + column) * self.bytes_per_pixel;
                    buffer[offset..offset + self.bytes_per_pixel]
                        .copy_from_slice(&bytes[..self.bytes_per_pixel]);
                }
            }
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    use core::ptr::NonNull;

    #[test]
    fn object_stack_starts_empty_and_popping_empty_preserves_empty() {
        let mut stack = ObjectStack::new();

        assert!(stack.is_empty());
        assert!(!stack.is_full());
        assert_eq!(stack.pop(), None);
        assert!(stack.is_empty());
    }

    #[test]
    fn object_stack_pushes_32_entries_and_rejects_33rd() {
        let mut values = [0u32; 33];
        let mut stack = ObjectStack::new();

        for value in values.iter_mut().take(32) {
            assert!(stack.push(NonNull::from(value)));
        }

        assert!(stack.is_full());
        let top_before = NonNull::from(&mut values[31]);
        assert!(!stack.push(NonNull::from(&mut values[32])));
        assert_eq!(stack.pop(), Some(top_before));

        for value in values[..31].iter_mut().rev() {
            assert_eq!(stack.pop(), Some(NonNull::from(value)));
        }

        assert_eq!(stack.pop(), None);
        assert!(stack.is_empty());
    }

    #[test]
    fn sparse_glyph_preserves_transparent_pixels_and_respects_pixel_size() {
        for bpp in [2, 4] {
            let surface = DebugSurface {
                offset: 4,
                stride: 8,
                width: 8,
                height: 8,
                bytes_per_pixel: bpp,
            };
            let mut actual = vec![0xaa; 4 + 64 * bpp + 3];
            let mut expected = actual.clone();
            let color = 0x44332211u32;
            for pixel in [0, 7, 56] {
                let offset = 4 + pixel * bpp;
                expected[offset..offset + bpp].copy_from_slice(&color.to_le_bytes()[..bpp]);
            }
            surface.draw_glyph(&mut actual, 0, 0, color, &[0x81, 0, 0, 0, 0, 0, 0, 1]);
            assert_eq!(actual, expected, "pixel size {}", bpp);
        }
    }

    #[test]
    fn invalid_geometry_and_overflow_leave_the_buffer_unchanged() {
        for problem in 0..12 {
            let mut surface = DebugSurface {
                offset: 0,
                stride: 8,
                width: 8,
                height: 8,
                bytes_per_pixel: 4,
            };
            let (mut x, mut y, mut glyph_len, mut buffer_len) = (0, 0, 8, 256);
            match problem {
                0 => x = -1,
                1 => y = -1,
                2 => x = 1,
                3 => y = 1,
                4 => surface.stride = 7,
                5 => surface.offset = usize::MAX,
                6 => surface.stride = usize::MAX,
                7 => surface.bytes_per_pixel = 1,
                8 => surface.bytes_per_pixel = 3,
                9 => glyph_len = 7,
                10 => glyph_len = 9,
                11 => buffer_len = 255,
                _ => unreachable!(),
            }
            let mut buffer = vec![0x5a; buffer_len];
            let original = buffer.clone();
            surface.draw_glyph(&mut buffer, x, y, 0x44332211, &vec![0xff; glyph_len]);
            assert_eq!(buffer, original, "invalid input case {}", problem);
        }
    }
}
