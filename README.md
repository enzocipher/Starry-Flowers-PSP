# Starry Flowers — PSP / Rust

Native Rust port for PSP, maintained on the `main` branch of [Starry-Flowers-PSP](https://github.com/enzocipher/Starry-Flowers-PSP). The PC version is available at [Starry-Flowers-but-in-Rust](https://github.com/enzocipher/Starry-Flowers-but-in-Rust).

The firmware is in `psp/`; the narrative engine and the layout it uses are included in `src/`. The root `Cargo.toml` only builds that library for host tests, without Macroquad or a PC application. All scripts run from the repository root, which has its own tracked `assets/` directory.

## Running

- ISO: `psp/dist/StarryFlowers.iso`, for PPSSPP or a PSP with compatible homebrew firmware and ISO support.
- Homebrew: copy `psp/dist/EBOOT.PBP` and the `psp/dist/DATA` directory to `PSP/GAME/StarryFlowers/` on the Memory Stick.
- Its save data is stored in `PSP/SAVEDATA/STARRYFLOWERS`. These are not Ren'Py or Windows save files.

The ISO and EBOOT include `ICON0.PNG` (144×80) and `PIC1.PNG` (480×272), prepared from the original logo and background so they are displayed in PPSSPP and the PSP menu.

The ISO includes a real MIPS PSP executable and converted resources from the included Starry Flowers 1.7.4 assets. The game does not require Python or Ren'Py at runtime.

## Releases and CI artifacts

GitHub Actions builds a complete ISO and homebrew ZIP, verifies the native executable, art, and packed resources, and generates `SHA256SUMS.txt`. The `StarryFlowers-PSP` Actions artifact contains `StarryFlowers.iso`, `StarryFlowers-homebrew.zip`, and `SHA256SUMS.txt`; download it from a PSP CI run. Pushing a new `v*` tag creates a draft GitHub Release with these files after tests pass; the owner reviews and publishes it. `workflow_dispatch` builds downloadable artifacts without creating a release.

The repository tracks the original Starry Flowers 1.7.4 source assets in `assets/`, including art, music, Ren'Py scripts, translations, fonts, and extracted inline emoji with their existing license notices. No original PC installation or Git LFS is required; a normal Git clone is sufficient. Compiled Ren'Py `*.rpyc` and `*.rpymc` files are excluded, and generated PSP `DATA`, `EBOOT`, and ISO files remain ignored.

Build prerequisites: Rust `nightly-2026-10-05-x86_64-pc-windows-gnu` with `rust-src`, `cargo-psp` 0.2.9, and the dependencies in `tools/requirements-psp.txt`. See the [releases](https://github.com/enzocipher/Starry-Flowers-PSP/releases).

To build and verify the same release files locally, run `./tools/ci-psp-build.ps1 -Python python`. For the homebrew ZIP, copy its `StarryFlowers` folder to `PSP/GAME/` on the Memory Stick. Asset credits and bundled license paths are listed in [ASSETS.md](ASSETS.md).

## Controls

| Control | Action |
|---|---|
| D-pad | Select options or accessories |
| X | Complete text, advance, or confirm |
| O / L | Go back one dialogue; O goes back in menus |
| Hold R | Skip read text |
| Select | Toggle skipping |
| Square | Toggle auto-advance |
| Triangle | Hide/show dialogue |
| Start | Menu, settings, and six save slots |
| Square / Triangle in accessories | Save/load favorite accessories |

English is the initial language; Spanish can be selected in Settings. Options include text speed, auto-advance, separate volume controls, mute all, and skip behavior. Settings use flower bars and the original controls, grouped for the PSP screen. Both initial routes, the chapters, epilogue, and eight extras are included, along with a gallery unlocked upon completion.

## Building on Windows

Requires Rust nightly with `rust-src`, `cargo-psp 0.2.9`, Python, and the tracked resources in `assets/`. It has been built with nightly **2026-10-05**, Windows GNU host. The Pillow, imageio-ffmpeg, and pycdlib versions used for preparation and packaging are pinned in `tools/requirements-psp.txt`.

```powershell
rustup toolchain install nightly-2026-10-05-x86_64-pc-windows-gnu --component rust-src --profile minimal
cargo install cargo-psp --version 0.2.9 --locked
python -m pip install -r tools/requirements-psp.txt
# From the repository root:
./tools/build_psp.ps1 -Python python
```

`prepare_psp.py` preserves the source art and converts it to PSP GE DXT5 tiles with mipmaps; it keeps the game's logical geometry at 0.375 scale, generates a Nunito atlas, and converts audio to 44.1 kHz stereo PCM. The cache uses content and configuration hashes to reuse unchanged images and audio. The manifest is validated before obsolete generated files from the previous manifest are removed; unknown files are preserved. `package_psp.py` generates the ISO and checks that `PSP_GAME/SYSDIR/EBOOT.BIN` contains the native ELF executable. Source game resources are tracked in Git; generated files remain excluded.

From the repository root, run manual preparation or pipeline tests as follows:

```powershell
python tools/prepare_psp.py
python -m unittest discover -s tools -p 'test_psp*.py'
```

The second preparation reuses resources whose content and recipe have not changed. To test audio blocks on the host without building the PSP firmware:

```powershell
$audioTest = Join-Path $env:TEMP 'starryflowers-audio-block-tests.exe'
rustc --test psp/src/audio_blocks.rs -o $audioTest
& $audioTest
```

## Memory and SDK

The copy of the narrative engine included in this repository is compiled, adapting its collections to `alloc::collections::BTreeMap`. The executable uses `no_std`, the PSP SDK for files, controls, display, and audio, an 18 MiB memory area, and a 6 MiB texture cache that accounts for the next tile before loading it. Three aligned 1 MiB surfaces keep the background, current scene, and previous scene during transitions; the most-used atlases remain cached. CPU and bus speeds of 333 MHz and 166 MHz are requested within SDK limits; this prioritizes performance over battery life.

`third_party/psp` comes from `psp 0.3.14` (MIT license included). Its original allocator created a kernel object for every allocation; the script exhausted the object limit while loading. The patch uses `linked_list_allocator` within a single reservation. Audio workers do not allocate memory during playback. Saves are first written to a temporary file and keep a backup during replacement.

The October 29, 2026 revision validates accessory, favorite, stack, and position indices before loading saves; it also checks a backup when the main JSON is readable but its state is invalid. It normalizes settings and limits automatic write retries to two seconds. Music retries opening and read errors with a 500 ms delay; repeated output errors re-reserve the channel. Normal effects EOF does not trigger repeats.

Glyphs and images share their file names through `Arc<str>`, avoiding another string allocation per glyph and per scene copy. Preparation v11 preserves source resolution and checks all three levels of each tile: if DXT5 exceeds the error threshold, it stores the full chain in RGBA. In the current resources, this is 5 of 2,567 tiles and 149,184 additional bytes. The verifier compares 7,701 levels against the original art and the ISO's 2,601 resources against the prepared files.

## Verification and limitations

`python tools/package_psp.py --audit` generates a separate ISO for automated tests. It boots in PPSSPP, captures the menu and first dialogue, plays through both routes and the eight extras, checks saving/loading and overwriting settings, and records played audio blocks. The result is written to `PSP/SAVEDATA/STARRYFLOWERS/AUDIT.JSON`. The normal ISO does not enable this test. `python tools/package_psp.py --performance-audit` runs the visual settings comparison, 120 navigation frames, the startup transition, and 120 dialogues with skipping and real rendering. It verifies that navigation and transition animation do not load textures or rebuild scenes. Save/load screens read saves once on entry and refresh the list after saving.

The renderer alternates between two screen buffers and uses a third buffer reserved for composing transitions, without writing to the one currently displayed. Outside blends, it draws textures at source resolution, preserving detail when scaling in PPSSPP. Each transition checks its source dialogue: a settings screen cannot act as the previous game scene. A dialogue with the same graphics updates its source without rebuilding the cache or repeating an old transition. Cancelling skip also does not restart skipped effects. Line layout uses glyph advances and a cache limited to 16 entries. The texture cache stays within its 6 MiB limit, keeps the name atlas, and writes to memory only the newly loaded texture.

Tests include 12 rounds between settings and the game in English/Spanish, comparing images, and transitions between empty scenes, mid-blend scenes, and dialogues with identical graphics. Captures use 16-byte-aligned memory for GE transfers. To repeat the tests with a PPSSPP installation, after building:

```powershell
./tools/test_psp.ps1 -Emulator 'C:/path/PPSSPPWindows64.exe' -Mode performance
./tools/test_psp.ps1 -Emulator 'C:/path/PPSSPPWindows64.exe' -Mode full -Resolution 3
./tools/test_psp.ps1 -Emulator 'C:/path/PPSSPPWindows64.exe' -Backend opengl
```

The script copies the emulator to a test environment inside `psp/test-emulator/runs`, using a 32 MiB PSP-1000 profile and no personal saves. It stores reports in `psp/dist` and terminates only the instance it started. `-Python` and `-TimeoutSeconds` can be specified when needed. Resource loads when changing scenes can still produce slower frames than navigation or already-loaded dialogues.

Testing uses the 32 MiB PSP-1000 profile in PPSSPP. Emulator verification does not replace testing on physical PSP hardware. Rendering uses the PSP GPU, bilinear filtering and mipmaps, transparency, and a scene cache in RAM at the native 480×272 resolution, avoiding the framebuffer aliasing that caused glitches in PPSSPP. Fonts and controls are drawn on top with the original atlases at four times their size. The original Windows resources are preserved; PSP uses art adapted to its resolution, stereo audio, English/Spanish, and a limited rollback of 32 dialogues; scene animations and the credits presentation are simplified. It does not yet have all of Windows' visual and language options.

Original story, art, and music: **NomnomNami**. Ending theme “Pretty in Pink”: **Marlene Bellissimo**. The authorship and license of the original resources are preserved.

The blue, red, and brown hearts are verified in their original dialogues. Twemoji graphics are from Twitter and contributors (CC-BY 4.0); the original attribution files are preserved alongside the prepared resources.

About is available from the initial menu and the in-game menu. Left/right or X cycles through the complete credits; O goes back. The authors of all 13 translations from the original are included, even though PSP supports English/Spanish gameplay, along with complete lists of testers, acknowledgements, and patrons. The original Ren'Py license is in `DATA/RENPY.TXT`.

Skipping advances at most every 80 ms. Cancelling it and stopping at unread text blocks R until it is released; skipped camera effects and transitions are not repeated. Read markers are saved every two seconds or when leaving the game, instead of writing for every dialogue. The stable background is kept separate from the portrait and dialogue box. Atlases are bound once per group of consecutive glyphs. The skip test requires less than 40 ms on average and 60 ms at the 95th percentile; results are in `verification.json`.
