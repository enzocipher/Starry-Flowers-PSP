use crate::engine::{clean_text, Sprite, State, Story};
use alloc::collections::BTreeMap as HashMap;
use alloc::{
    format,
    string::{String, ToString},
    sync::Arc,
    vec,
    vec::Vec,
};
use serde::Deserialize;

pub const W: usize = 480;
pub const H: usize = 272;
pub const INK: u32 = 0xff5c3638;
pub const WHITE: u32 = 0xff_ffffff;
pub const BLUE: u32 = 0xffffa358;

#[derive(Clone, Deserialize)]
pub struct Tile {
    pub file: Arc<str>,
    pub x: usize,
    pub y: usize,
    pub width: usize,
    pub height: usize,
    pub texture_width: usize,
    pub texture_height: usize,
    #[serde(default)]
    pub dxt5: bool,
}
#[derive(Clone, Deserialize)]
pub struct ImageInfo {
    pub width: usize,
    pub height: usize,
    pub original_width: usize,
    pub original_height: usize,
    #[serde(default)]
    pub raster_width: usize,
    #[serde(default)]
    pub raster_height: usize,
    pub tiles: Vec<Tile>,
}
#[derive(Deserialize)]
pub struct Glyph {
    pub file: Arc<str>,
    pub x: usize,
    pub y: usize,
    pub width: usize,
    pub height: usize,
    pub left: f32,
    pub top: f32,
    pub advance: f32,
}
#[derive(Deserialize)]
pub struct Font {
    pub scale: f32,
    pub ascent: f32,
    pub glyphs: HashMap<char, Glyph>,
}
#[derive(Deserialize)]
pub struct Manifest {
    pub images: HashMap<String, ImageInfo>,
    pub fonts: HashMap<String, Font>,
    pub audio: HashMap<String, String>,
    pub inline_symbols: HashMap<char, crate::engine::InlineSymbol>,
}
pub struct Renderer {
    pub frame: crate::gpu::Frame,
    pub manifest: Manifest,
    root: String,
    gpu: crate::gpu::Gpu,
    last_buffer: usize,
    wraps: Vec<Wrapped>,
}
struct Wrapped {
    text: String,
    size: usize,
    width: u32,
    lines: Arc<Vec<crate::layout::Line>>,
}
impl Renderer {
    pub fn new(root: &str) -> Self {
        let manifest = serde_json::from_slice(
            &crate::io::read(format!("{root}/DATA/MANIFEST.JSON")).expect("Missing PSP assets"),
        )
        .unwrap();
        Self {
            frame: crate::gpu::Frame::new(),
            manifest,
            root: root.into(),
            gpu: crate::gpu::Gpu::new(),
            last_buffer: 0,
            wraps: Vec::new(),
        }
    }
    pub fn image(
        &mut self,
        name: &str,
        x: i32,
        y: i32,
        size: Option<(usize, usize)>,
        alpha: u32,
        flip: bool,
    ) {
        let Some(info) = self.manifest.images.get(name) else {
            return;
        };
        let (w, h) = size.unwrap_or((info.width, info.height));
        self.image_at(name, x as f32, y as f32, (w as f32, h as f32), alpha, flip);
    }
    pub fn image_at(
        &mut self,
        name: &str,
        x: f32,
        y: f32,
        size: (f32, f32),
        alpha: u32,
        flip: bool,
    ) {
        let Some(info) = self.manifest.images.get(name) else {
            return;
        };
        let (w, h) = size;
        let rw = if info.raster_width > 0 {
            info.raster_width
        } else {
            info.original_width
        };
        let rh = if info.raster_height > 0 {
            info.raster_height
        } else {
            info.original_height
        };
        let sx = w / rw as f32;
        let sy = h / rh as f32;
        for t in &info.tiles {
            let left = if flip { rw - t.x - t.width } else { t.x };
            self.frame.draws.push(crate::gpu::Draw {
                file: t.file.clone(),
                tw: t.texture_width,
                th: t.texture_height,
                font: false,
                dxt5: t.dxt5,
                xy: [
                    x + left as f32 * sx,
                    y + t.y as f32 * sy,
                    x + (left + t.width) as f32 * sx,
                    y + (t.y + t.height) as f32 * sy,
                ],
                uv: if flip {
                    [4. + t.width as f32, 4., 4., 4. + t.height as f32]
                } else {
                    [4., 4., 4. + t.width as f32, 4. + t.height as f32]
                },
                color: (alpha << 24) | 0xffffff,
            });
        }
        if name.contains("_face_") {
            self.frame.prefix_sealed = true;
        }
        if !self.frame.prefix_sealed {
            self.frame.prefix_len = self.frame.draws.len();
        }
    }
    pub fn rect(&mut self, x: i32, y: i32, w: usize, h: usize, color: u32) {
        self.frame.draws.push(crate::gpu::Draw {
            file: "".into(),
            tw: 0,
            th: 0,
            font: false,
            dxt5: false,
            xy: [
                x as f32,
                y as f32,
                (x + w as i32) as f32,
                (y + h as i32) as f32,
            ],
            uv: [0.; 4],
            color,
        });
    }
    pub fn width(&self, text: &str, size: usize) -> f32 {
        let font = &self.manifest.fonts[&size.to_string()];
        text.chars().map(|c| self.advance(font, c, size)).sum()
    }
    fn advance(&self, font: &Font, c: char, size: usize) -> f32 {
        if c == '\u{fe0f}' {
            return 0.;
        }
        self.manifest
            .inline_symbols
            .get(&c)
            .map(|symbol| symbol.advance * size as f32)
            .unwrap_or_else(|| {
                font.glyphs
                    .get(&c)
                    .map(|g| g.advance)
                    .unwrap_or(size as f32 * 0.5)
            })
    }
    fn wrapped(&mut self, text: &str, width: f32, size: usize) -> Arc<Vec<crate::layout::Line>> {
        if let Some(index) = self
            .wraps
            .iter()
            .position(|w| w.text == text && w.width == width.to_bits() && w.size == size)
        {
            let hit = self.wraps.remove(index);
            let lines = hit.lines.clone();
            self.wraps.push(hit);
            return lines;
        }
        let font = &self.manifest.fonts[&size.to_string()];
        let lines = Arc::new(crate::layout::wrap_advances(text, width, |c| {
            self.advance(font, c, size)
        }));
        if self.wraps.len() == 16 {
            self.wraps.remove(0);
        }
        self.wraps.push(Wrapped {
            text: text.into(),
            size,
            width: width.to_bits(),
            lines: lines.clone(),
        });
        lines
    }
    pub fn text(&mut self, text: &str, x: i32, y: i32, size: usize, color: u32) {
        let font_key = size.to_string();
        let scale = self.manifest.fonts[&font_key].scale;
        let ascent = self.manifest.fonts[&font_key].ascent;
        let mut cursor = x as f32;
        for c in text.chars() {
            if c == '\u{fe0f}' {
                continue;
            }
            if let Some(symbol) = self.manifest.inline_symbols.get(&c).cloned() {
                let start = self.frame.draws.len();
                let old = (self.frame.prefix_len, self.frame.prefix_sealed);
                self.image_at(
                    &symbol.image,
                    cursor,
                    y as f32 + ascent + symbol.baseline_top * size as f32,
                    (symbol.width * size as f32, symbol.height * size as f32),
                    color >> 24,
                    false,
                );
                (self.frame.prefix_len, self.frame.prefix_sealed) = old;
                if symbol.tint {
                    for d in &mut self.frame.draws[start..] {
                        d.color = color;
                    }
                }
                cursor += symbol.advance * size as f32;
                continue;
            }
            let Some(g) = self.manifest.fonts[&font_key].glyphs.get(&c) else {
                cursor += size as f32 * 0.5;
                continue;
            };
            let left = cursor + g.left;
            let top = y as f32 + g.top;
            self.frame.draws.push(crate::gpu::Draw {
                file: g.file.clone(),
                tw: 512,
                th: 512,
                font: true,
                dxt5: false,
                xy: [
                    left,
                    top,
                    left + g.width as f32 / scale,
                    top + g.height as f32 / scale,
                ],
                uv: [
                    g.x as f32,
                    g.y as f32,
                    (g.x + g.width) as f32,
                    (g.y + g.height) as f32,
                ],
                color,
            });
            cursor += g.advance;
        }
    }
    pub fn image_progress(&mut self, name: &str, x: f32, y: f32, w: f32, h: f32, fraction: f32) {
        let start = self.frame.draws.len();
        let old = (self.frame.prefix_len, self.frame.prefix_sealed);
        self.image_at(name, x, y, (w, h), 255, false);
        (self.frame.prefix_len, self.frame.prefix_sealed) = old;
        let right = x + w * fraction.clamp(0., 1.);
        for d in &mut self.frame.draws[start..] {
            let original = d.xy[2];
            let clipped = original.min(right).max(d.xy[0]);
            let ratio = (clipped - d.xy[0]) / (original - d.xy[0]);
            d.xy[2] = clipped;
            d.uv[2] = d.uv[0] + (d.uv[2] - d.uv[0]) * ratio;
        }
    }
    pub fn label(&mut self, text: &str, x: i32, y: i32, width: f32, size: usize, color: u32) {
        if width <= 0. {
            return;
        }
        let size = [size, 10, 8]
            .into_iter()
            .find(|s| self.width(text, *s) <= width)
            .unwrap_or(8);
        let start = self.frame.draws.len();
        self.text(text, x, y, size, color);
        // Glyph bearings can exceed the advance; fit actual ink as well as spacing.
        let mut left = x as f32;
        let mut right = x as f32 + self.width(text, size);
        for d in &self.frame.draws[start..] {
            left = left.min(d.xy[0]);
            right = right.max(d.xy[2]);
        }
        let scale = (width / (right - left).max(1.)).min(1.);
        for d in &mut self.frame.draws[start..] {
            d.xy[0] = x as f32 + (d.xy[0] - left) * scale;
            d.xy[2] = x as f32 + (d.xy[2] - left) * scale;
            d.xy[1] = y as f32 + (d.xy[1] - y as f32) * scale;
            d.xy[3] = y as f32 + (d.xy[3] - y as f32) * scale;
        }
    }
    pub fn name(&mut self, who: &str, text: &str, x: i32, y: i32) {
        let (outer, inner) = match who {
            "p" => (0xffeddaff, 0xff754db8),
            "w" => (0xffffdbbe, 0xffc18350),
            "a" => (0xffffdaf3, 0xff9858a2),
            "c" => (0xffdae3ff, 0xff5866a2),
            _ => (0xffffdbbe, 0xffc18350),
        };
        for (radius, color) in [(3, outer), (1, inner)] {
            for (dx, dy) in [
                (-radius, 0),
                (radius, 0),
                (0, -radius),
                (0, radius),
                (-radius, -radius),
                (radius, radius),
                (-radius, radius),
                (radius, -radius),
            ] {
                self.text(text, x + dx, y + dy, 14, color);
            }
        }
        self.text(text, x, y, 14, WHITE);
    }
    pub fn flow(
        &mut self,
        text: &str,
        x: i32,
        y: i32,
        width: f32,
        height: usize,
        revealed: usize,
        color: u32,
    ) -> usize {
        let text = clean_text(text);
        let (size, lines) = [12, 10]
            .into_iter()
            .map(|size| (size, self.wrapped(&text, width, size)))
            .find(|(s, l)| l.len() * (s * 14 / 10) <= height)
            .unwrap_or_else(|| (10, self.wrapped(&text, width, 10)));
        for (i, line) in lines.iter().enumerate() {
            let n = revealed
                .saturating_sub(line.start)
                .min(line.end - line.start);
            let end = if n == line.end - line.start {
                line.text.len()
            } else {
                line.text
                    .char_indices()
                    .nth(n)
                    .map(|(byte, _)| byte)
                    .unwrap_or(line.text.len())
            };
            self.text(
                &line.text[..end],
                x,
                y + (i * size * 14 / 10) as i32,
                size,
                color,
            );
        }
        lines.len() * size * 14 / 10
    }
    pub fn scene(&mut self, state: &State, story: &Story) {
        self.frame.fill(0xff000000);
        for category in 0..5 {
            for s in &state.sprites {
                let cat = match s.tag.as_str() {
                    "bg" | "black" | "white" => 0,
                    "cg" => 2,
                    "fg" => 3,
                    "title" | "cinebars" | "lyrics" | "tld" | "cred1" | "cred2" | "cred6"
                    | "cred7" | "credscroll" => 4,
                    _ => 1,
                };
                if cat != category {
                    continue;
                }
                if s.tag == "white" {
                    self.frame.fill(WHITE);
                }
                for name in layers(s, state, story) {
                    let Some(info) = self.manifest.images.get(&name) else {
                        continue;
                    };
                    let (w, h) = (info.width, info.height);
                    let (x, y, size) = match s.tag.as_str() {
                        "bg" => (
                            0,
                            if s.position == "top" {
                                0
                            } else {
                                270 - h as i32
                            },
                            Some((480, h)),
                        ),
                        "cg" if info.original_width >= 1200 => {
                            (0, (270 - h as i32) / 2, Some((480, h)))
                        }
                        "cg" => (
                            (480 - w as i32) / 2,
                            if info.original_height < 500 {
                                30
                            } else {
                                270 - h as i32
                            },
                            None,
                        ),
                        "fg" => (0, 270 - h as i32, None),
                        _ => (
                            if s.position.starts_with("left") {
                                0
                            } else {
                                ((480 - w as i32) as f32 * 0.85) as i32
                            },
                            270 - h as i32,
                            None,
                        ),
                    };
                    self.image(&name, x, y, size, 255, s.position == "flip");
                }
                let key = core::iter::once(s.tag.as_str())
                    .chain(s.attrs.iter().map(|s| s.as_str()))
                    .collect::<Vec<_>>()
                    .join(" ");
                if let Some(text) = story.text_images.get(&key) {
                    self.flow(
                        text,
                        45,
                        if s.tag == "title" { 110 } else { 55 },
                        390.,
                        160,
                        usize::MAX,
                        WHITE,
                    );
                }
                if s.tag == "cinebars" {
                    self.rect(0, 0, 480, 22, 0xff000000);
                    self.rect(0, 248, 480, 22, 0xff000000);
                }
            }
        }
        self.frame.scene_len = self.frame.draws.len();
        // Distinguish successive lines even when their backgrounds/portraits are identical.
        self.frame.origin = Some(
            self.frame
                .signature(self.frame.scene_len)
                .wrapping_mul(1099511628211)
                .wrapping_add(state.pc as u64),
        );
    }
    pub fn dialogue(&mut self, state: &State, story: &Story, lang: &str, revealed: usize) {
        // Textbox height and portrait change per line; never include them in the stable prefix.
        self.frame.prefix_sealed = true;
        if state.nvl_mode {
            self.image("ui nvl", 0, 0, Some((480, 272)), 255, false);
            self.frame.scene_len = self.frame.draws.len();
            let paragraphs: Vec<_> = state
                .nvl
                .iter()
                .map(|s| clean_text(&story.translate(s, lang)))
                .collect();
            let prefix = paragraphs
                .iter()
                .take(paragraphs.len().saturating_sub(1))
                .map(|s| s.chars().count() + 2)
                .sum::<usize>();
            self.flow(
                &paragraphs.join("\n\n"),
                90,
                18,
                293.,
                230,
                prefix + revealed,
                INK,
            );
            return;
        }
        let text = story.translate(&state.text, lang);
        if state.who == "centered" {
            self.flow(&text, 48, 105, 384., 150, revealed, WHITE);
            return;
        }
        let lines = self.wrapped(&clean_text(&text), 260., 12);
        let height = (lines.len() * 17 + 36).clamp(75, 140);
        let top = 270 - height as i32;
        self.image(
            "ui textbox",
            0,
            top + 6,
            Some((480, height - 6)),
            255,
            false,
        );
        if state.who == "w" {
            let sprite = Sprite {
                tag: "side_peri".into(),
                attrs: state.attrs.clone(),
                position: String::new(),
            };
            for name in layers(&sprite, state, story) {
                self.image(&name, 0, 135, Some((135, 135)), 255, false);
            }
        }
        if !state.who.is_empty() && state.who != "n" {
            let name = match state.who.as_str() {
                "p" => "Pastille",
                "w" => "Periwinkle",
                "a" => "Astragalus",
                "c" => "Cassia",
                "j" => "Jam",
                "k" => "Kardaemon",
                "r" => "Amaretti",
                "u" => "Nasty Witch",
                "h" => "Himbo Witch",
                "g" => "Gumdrop",
                _ => "",
            };
            let name = story.translate(name, lang);
            self.name(&state.who, &name, 129, top - 17);
        }
        self.frame.scene_len = self.frame.draws.len();
        self.flow(
            &text,
            142,
            top + 10,
            260.,
            height - 27,
            revealed,
            if state.who == "n" { 0xff987779 } else { INK },
        );
    }
    pub fn stats(&self) -> (usize, usize) {
        (self.gpu.texture_loads, self.gpu.scene_renders)
    }
    pub fn load_stats(&self) -> (f64, f64, usize) {
        (
            self.gpu.load_ms,
            self.gpu.inflate_ms,
            self.gpu.prefix_renders,
        )
    }
    pub fn present(&mut self, buffer: usize) {
        let _ = buffer;
        let next = 1 - self.last_buffer;
        self.gpu.present(&self.frame, &self.root, next);
        self.last_buffer = next;
    }
    pub fn pixels(&mut self) -> Vec<u32> {
        self.present(self.last_buffer);
        self.gpu.pixels(self.last_buffer)
    }
}
pub fn layers(sprite: &Sprite, state: &State, story: &Story) -> Vec<String> {
    if sprite.tag == "pastille" || sprite.tag == "side_peri" {
        let prefix = &sprite.tag;
        let mut names = vec![format!("{prefix}_base")];
        if prefix == "side_peri" {
            names.push(story.accessories[1][state.acc[1]].clone());
        }
        for (group, default) in [("outfit", "witch"), ("face", "smile")] {
            let attr = sprite
                .attrs
                .iter()
                .find(|a| story.images.contains_key(&format!("{prefix}_{group}_{a}")))
                .map(String::as_str)
                .unwrap_or(default);
            names.push(format!("{prefix}_{group}_{attr}"));
        }
        if prefix == "side_peri" {
            names.push(story.accessories[0][state.acc[0]].clone());
            names.push(story.accessories[2][state.acc[2]].clone());
        }
        names
    } else {
        let name = core::iter::once(sprite.tag.as_str())
            .chain(sprite.attrs.iter().map(String::as_str))
            .collect::<Vec<_>>()
            .join(" ");
        if story.images.contains_key(&name) {
            vec![name]
        } else {
            vec![]
        }
    }
}
