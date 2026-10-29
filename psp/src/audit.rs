//! Executes on the emulated PSP, including its allocator and Memory Stick I/O.
use crate::{
    engine::{State, Stop, Story},
    load,
    render::{Renderer, INK},
    save, screenshot, Prefs,
};
use alloc::{format, vec};

pub fn run(renderer: &mut Renderer, story: &Story) -> serde_json::Value {
    persistence_regression(story);
    audio_recovery_regression();
    let mut lines = 0usize;
    let mut symbols_seen = vec![];
    let mut decisions = 0usize;
    let mut outfits = 0usize;
    let mut finishes = 0usize;
    for branch in 0..2 {
        let mut state = State::default();
        state.start(story, "start");
        let mut sample = false;
        for _ in 0..12000 {
            match state.run(story) {
                Stop::Say => {
                    lines += 1;
                    for (symbol, name) in [
                        ('\u{1f499}', "BLUE"),
                        ('\u{2764}', "RED"),
                        ('\u{1f90e}', "BROWN"),
                    ] {
                        if state.text.contains(symbol) && !symbols_seen.contains(&symbol) {
                            renderer.scene(&state, story);
                            renderer.dialogue(&state, story, "", usize::MAX);
                            screenshot(renderer, &format!("PSP-HEART-{name}"));
                            symbols_seen.push(symbol);
                        }
                    }
                    if !sample && state.who == "p" {
                        renderer.scene(&state, story);
                        renderer.dialogue(&state, story, "", usize::MAX);
                        screenshot(renderer, &format!("PSP-PASTILLE-{branch}"));
                        assert!(save("AUDIT-SLOT", &state));
                        let restored: State = load("AUDIT-SLOT").expect("Save reload failed");
                        assert_eq!(restored.pc, state.pc);
                        assert_eq!(restored.text, state.text);
                        sample = true;
                    }
                    if lines % 200 == 0 {
                        renderer.scene(&state, story);
                        renderer.dialogue(&state, story, "es", usize::MAX);
                        renderer.present(0);
                    }
                }
                Stop::Menu => {
                    decisions += 1;
                    let choices = &story.ops[state.pc - 1].choices;
                    state.pc = choices[branch.min(choices.len() - 1)].target;
                }
                Stop::Dress => {
                    outfits += 1;
                    state.acc = [branch; 3];
                    if outfits == 1 || outfits == 5 {
                        crate::dress_scene(renderer, &state, story);
                        screenshot(renderer, &format!("PSP-ACCESSORIES-{branch}"));
                    }
                }
                Stop::End => {
                    finishes += 1;
                    break;
                }
                _ => {}
            }
        }
    }
    assert_eq!(finishes, 2);
    assert_eq!(symbols_seen.len(), 3);
    let mut extras = 0usize;
    for extra in crate::EXTRAS {
        let mut state = State::default();
        state.start(story, extra);
        for _ in 0..2000 {
            match state.run(story) {
                Stop::Say => {
                    lines += 1;
                }
                Stop::Menu => {
                    state.pc = story.ops[state.pc - 1].choices[0].target;
                }
                Stop::End | Stop::Gallery => {
                    extras += 1;
                    break;
                }
                _ => {}
            }
        }
    }
    assert_eq!(extras, 8);
    let mut prefs = Prefs {
        read: vec![15, 22],
        ..Default::default()
    };
    assert!(save("AUDIT-PREFS", &prefs));
    prefs.lang = "es".into();
    prefs.mute = true;
    assert!(save("AUDIT-PREFS", &prefs));
    let restored: Prefs = load("AUDIT-PREFS").unwrap();
    assert_eq!(restored.lang, "es");
    assert!(restored.mute);
    assert_eq!(restored.read, prefs.read);
    crate::settings_scene(renderer, story, &Prefs::default(), 0);
    screenshot(renderer, "PSP-SETTINGS");
    let mut preview = Prefs::default();
    preview.lang = "es".into();
    preview.cps = 0.;
    preview.mute = true;
    crate::settings_scene(renderer, story, &preview, 8);
    screenshot(renderer, "PSP-SETTINGS-ES");
    for index in 0..story.credits.len() {
        crate::about_scene(renderer, story, "", index);
        screenshot(renderer, &format!("PSP-ABOUT-{}", index));
    }
    let skip_perf = skip_playback(renderer, story);
    let perf = performance(renderer, story);
    renderer.frame.fill(0xffffffff);
    renderer.text("PSP audit passed", 25, 25, 18, INK);
    renderer.text(
        &format!("{lines} lines; {finishes} endings; {extras} extras"),
        25,
        65,
        12,
        INK,
    );
    renderer.present(0);
    screenshot(renderer, "PSP-AUDIT-PASSED");
    serde_json::json!({"passed":true,"dialogues":lines,"endings":finishes,"extras":extras,"decisions":decisions,"accessory_screens":outfits,"save_reload":true,"settings_overwrite":true,"invalid_saves_rejected":true,"semantic_backup_recovery":true,"preferences_normalized":true,"audio_open_recovery":true,"inline_symbols":symbols_seen.len(),"performance":perf,"skip_playback":skip_perf,
        "cpu_mhz":unsafe { psp::sys::scePowerGetCpuClockFrequencyInt() },
        "bus_mhz":unsafe { psp::sys::scePowerGetBusClockFrequencyInt() }})
}

fn audio_recovery_regression() {
    let root = crate::io::save_dir();
    let data_dir = alloc::format!("{root}/DATA");
    crate::io::mkdir(&data_dir);
    let source = alloc::format!("{data_dir}/AUDIT-RECOVERY.PCM");
    crate::io::remove(&source);
    let mut files = alloc::collections::BTreeMap::new();
    files.insert("test".into(), "AUDIT-RECOVERY.PCM".into());
    let audio = crate::audio::Audio::new(&root, &files, true);
    audio.update("AUDIT-RECOVERY.PCM", 0., false);
    unsafe {
        psp::sys::sceKernelDelayThread(600_000);
    }
    assert_eq!(audio.blocks(), 0);
    crate::io::write(&source, &[0; 4096]).unwrap();
    let deadline = crate::now() + 2.;
    while audio.blocks() == 0 && crate::now() < deadline {
        unsafe {
            psp::sys::sceKernelDelayThread(10_000);
        }
    }
    assert!(audio.blocks() > 0, "Music did not retry a failed open");
    audio.update("", 0., false);
    unsafe {
        psp::sys::sceKernelDelayThread(50_000);
    }
    crate::io::remove(&source);
}

fn persistence_regression(story: &Story) {
    let mut prefs = Prefs {
        lang: "invalid".into(),
        cps: -50.,
        delay: 100.,
        music: -1.,
        sound: 3.,
        fave: [usize::MAX; 3],
        read: vec![12, 3, 12, story.ops.len() + 1],
        ..Default::default()
    };
    prefs.normalize(story);
    assert!(prefs.lang.is_empty());
    assert_eq!(
        (prefs.cps, prefs.delay, prefs.music, prefs.sound),
        (0., 30., 0., 1.)
    );
    assert_eq!(prefs.fave, [0; 3]);
    assert_eq!(prefs.read, vec![3, 12]);
    assert!(!prefs.mark_read(12));
    assert!(prefs.mark_read(7));
    assert_eq!(prefs.read, vec![3, 7, 12]);
    let mut state = State::default();
    state.start(story, "start");
    state.run(story);
    assert!(crate::valid_save(story, &state));
    let valid = state.clone();
    state.acc[1] = usize::MAX;
    assert!(!crate::valid_save(story, &state));
    assert!(save("AUDIT-INVALID", &state));
    assert!(
        crate::load_checked::<State>("AUDIT-INVALID", |s| crate::valid_save(story, s)).is_none()
    );
    // A valid backup must be considered even when primary JSON parses correctly.
    let backup = alloc::format!("{}/AUDIT-INVALID.JSON.BAK", crate::io::save_dir());
    crate::io::write(&backup, &serde_json::to_vec(&valid).unwrap()).unwrap();
    assert_eq!(
        crate::load_checked::<State>("AUDIT-INVALID", |s| crate::valid_save(story, s))
            .unwrap()
            .pc,
        valid.pc
    );
    crate::io::remove(&backup);
    state = valid.clone();
    state.fave[2] = usize::MAX;
    assert!(!crate::valid_save(story, &state));
    state = valid.clone();
    state.stack.push(story.ops.len() + 1);
    assert!(!crate::valid_save(story, &state));
    state = valid;
    state.pc = 0;
    assert!(!crate::valid_save(story, &state));
}

pub fn performance(renderer: &mut Renderer, story: &Story) -> serde_json::Value {
    transition_regression(renderer);
    let menu_return = menu_return_regression(renderer, story);
    let mut preview = Prefs::default();
    preview.lang = "es".into();
    preview.mute = true;
    preview.cps = 0.;
    // Compare the retained scene with a direct draw, then exercise navigation.
    crate::settings_scene(renderer, story, &preview, 8);
    let cached = renderer.pixels();
    screenshot(renderer, "PSP-SETTINGS-CACHED");
    renderer.frame.scene_len = 0;
    let direct = renderer.pixels();
    screenshot(renderer, "PSP-SETTINGS-DIRECT");
    let differences = cached
        .iter()
        .zip(&direct)
        .filter(|(a, b)| {
            [0, 8, 16].iter().any(|shift| {
                (((**a >> shift) & 255) as i32 - ((**b >> shift) & 255) as i32).abs() > 3
            })
        })
        .count();
    let severe = cached
        .iter()
        .zip(&direct)
        .filter(|(a, b)| {
            [0, 8, 16].iter().any(|shift| {
                (((**a >> shift) & 255) as i32 - ((**b >> shift) & 255) as i32).abs() > 30
            })
        })
        .count();
    let error: usize = cached
        .iter()
        .zip(&direct)
        .map(|(a, b)| {
            [0, 8, 16]
                .iter()
                .map(|shift| {
                    (((*a >> shift) & 255) as i32 - ((*b >> shift) & 255) as i32).unsigned_abs()
                        as usize
                })
                .sum::<usize>()
        })
        .sum();
    let mean_error = error as f64 / (480. * 272. * 3.);
    assert!(
        severe < 480 && mean_error < 2.,
        "Cached settings are corrupted"
    );
    save(
        "PERF-CACHE",
        &serde_json::json!({"different_pixels":differences}),
    );
    drop(cached);
    drop(direct);
    for i in 0..20 {
        crate::settings_scene(renderer, story, &preview, i % 10);
        renderer.present(1);
    }
    let before = renderer.stats();
    let began = crate::now();
    for i in 0..120 {
        crate::settings_scene(renderer, story, &preview, i % 10);
        renderer.present(1);
    }
    let navigation_ms = (crate::now() - began) * 1000. / 120.;
    let after = renderer.stats();
    assert_eq!(before.0, after.0, "Navigating settings reloaded textures");
    assert_eq!(
        before.1, after.1,
        "Navigating settings rebuilt the background"
    );
    screenshot(renderer, "PSP-SETTINGS-NAVIGATION");
    let mut startup = State::default();
    startup.start(story, "start");
    for _ in 0..200 {
        if startup.run(story) == Stop::Say && startup.who == "w" {
            break;
        }
    }
    assert_eq!(startup.who, "w");
    renderer.scene(&startup, story);
    renderer.dialogue(&startup, story, "", usize::MAX);
    let startup_frame = renderer.frame.clone();
    renderer.frame.fade_from(&startup_frame, 0);
    renderer.present(1);
    let startup_before = renderer.stats();
    for alpha in [32, 64, 96, 128, 160, 192, 224, 255] {
        renderer.frame.clone_from(&startup_frame);
        renderer.frame.fade_from(&startup_frame, alpha);
        renderer.present(1);
        if alpha == 128 {
            screenshot(renderer, "PSP-STARTUP-FADE");
        }
    }
    let startup_after = renderer.stats();
    assert_eq!(
        startup_before, startup_after,
        "Startup fade reloaded the scene"
    );
    screenshot(renderer, "PSP-STARTUP-FINAL");
    serde_json::json!({"menu_return":menu_return,"settings_cache_different_pixels":differences,"settings_cache_mean_rgb_error":mean_error,"settings_cache_severe_pixels":severe,"startup_fade_texture_loads":startup_after.0-startup_before.0,"startup_fade_scene_renders":startup_after.1-startup_before.1,"settings_navigation_ms_per_frame":navigation_ms,"settings_navigation_texture_loads":after.0-before.0,"settings_navigation_scene_renders":after.1-before.1})
}

fn transition_regression(renderer: &mut Renderer) {
    // Valid game-to-game fades must survive the menu-contamination fix, including empty scenes.
    renderer.frame.fill(0xff604020);
    renderer.frame.origin = Some(renderer.frame.signature(0));
    let old = renderer.frame.clone();
    let reference = renderer.pixels();
    renderer.frame.fill(0xff2060a0);
    renderer.frame.origin = Some(renderer.frame.signature(0));
    let next = renderer.frame.clone();
    renderer.frame.fade_from(&old, 0);
    let faded = renderer.pixels();
    assert!(
        reference
            .iter()
            .zip(&faded)
            .all(|(a, b)| a & 0xffffff == b & 0xffffff),
        "Game fade lost its source scene"
    );
    renderer.frame.clone_from(&next);
    renderer.frame.fade_from(&old, 128);
    let middle = renderer.pixels();
    for pixel in &middle {
        for (shift, expected) in [(0, 96i32), (8, 80), (16, 64)] {
            assert!(
                (((*pixel >> shift) & 255) as i32 - expected).abs() <= 2,
                "Game fade did not blend both scenes"
            );
        }
    }
    renderer.frame.clone_from(&next);
    let complete = renderer.pixels();
    assert!(
        complete.iter().all(|p| p & 0xffffff == 0x2060a0),
        "Game fade did not finish"
    );
    renderer.frame.origin = Some(next.origin.unwrap().wrapping_add(1));
    let repeated = renderer.frame.clone();
    renderer.frame.fade_from(&next, 0);
    let unchanged = renderer.pixels();
    assert!(
        unchanged.iter().all(|p| p & 0xffffff == 0x2060a0),
        "Unchanged dialogue replayed an obsolete fade"
    );
    renderer.frame.fill(0xff404040);
    renderer.frame.origin = Some(renderer.frame.signature(0));
    renderer.frame.fade_from(&repeated, 0);
    let following = renderer.pixels();
    assert!(
        following.iter().all(|p| p & 0xffffff == 0x2060a0),
        "Cached dialogue lost transition provenance"
    );
}

fn menu_return_regression(renderer: &mut Renderer, story: &Story) -> serde_json::Value {
    let mut state = State::default();
    state.start(story, "start");
    for _ in 0..200 {
        if state.run(story) == Stop::Say && state.who == "w" {
            break;
        }
    }
    assert_eq!(state.who, "w");
    renderer.scene(&state, story);
    let base = renderer.frame.clone();
    renderer.dialogue(&state, story, "", usize::MAX);
    let game = renderer.frame.clone();
    let reference = renderer.pixels();
    screenshot(renderer, "PSP-MENU-REFERENCE");
    let mut worst_error = 0f64;
    for iteration in 0..12 {
        let mut prefs = Prefs::default();
        if iteration % 2 == 1 {
            prefs.lang = "es".into();
        }
        crate::settings_scene(renderer, story, &prefs, iteration % 10);
        renderer.present(1);
        renderer.frame.clone_from(&game);
        // The main loop may still request a fade after returning or cancelling skip.
        renderer.frame.fade_from(&base, 0);
        let returned = renderer.pixels();
        let error: usize = reference
            .iter()
            .zip(&returned)
            .map(|(a, b)| {
                [0, 8, 16]
                    .iter()
                    .map(|shift| {
                        (((*a >> shift) & 255) as i32 - ((*b >> shift) & 255) as i32).unsigned_abs()
                            as usize
                    })
                    .sum::<usize>()
            })
            .sum();
        let mean_error = error as f64 / (480. * 272. * 3.);
        worst_error = worst_error.max(mean_error);
        save(
            "MENU-RETURN",
            &serde_json::json!({"iteration":iteration,"mean_rgb_error":mean_error}),
        );
        if iteration == 0 {
            screenshot(renderer, "PSP-MENU-RETURN");
        }
        assert!(mean_error < 2., "Settings background leaked into gameplay");
        renderer.frame.clone_from(&game);
        renderer.present(1);
    }
    serde_json::json!({"returns":12,"worst_mean_rgb_error":worst_error})
}

pub fn skip_playback(renderer: &mut Renderer, story: &Story) -> serde_json::Value {
    let mut gate = crate::playback::SkipGate::default();
    let mut latched = false;
    assert!(gate.update(&mut latched, true, false, false, true));
    assert!(!gate.update(&mut latched, true, false, true, true));
    assert!(!gate.update(&mut latched, true, false, false, true));
    gate.update(&mut latched, false, false, false, true);
    assert!(!gate.update(&mut latched, true, false, false, false));
    assert!(!gate.update(&mut latched, true, false, false, true));
    gate.update(&mut latched, false, false, false, true);
    let mut state = State::default();
    state.start(story, "start");
    let mut stop = state.run(story);
    let mut dialogues = 0usize;
    let mut frames = 0usize;
    let mut next_scene = true;
    let began = crate::now();
    let before = renderer.stats();
    let load_before = renderer.load_stats();
    let mut durations = vec![];
    while dialogues < 120 && frames < 1800 {
        let frame_started = crate::now();
        if next_scene {
            renderer.scene(&state, story);
            next_scene = false;
        }
        let base = renderer.frame.clone();
        if stop == Stop::Say {
            renderer.dialogue(&state, story, "", usize::MAX);
        }
        renderer.present(1);
        renderer.frame = base;
        let active = gate.update(&mut latched, true, false, false, true);
        if gate.advance_due(active, crate::now()) {
            match stop {
                Stop::Menu => {
                    state.pc = story.ops[state.pc - 1].choices[0].target;
                }
                Stop::Dress => {
                    state.acc = [0; 3];
                }
                Stop::Say => {
                    dialogues += 1;
                }
                Stop::End => break,
                _ => {}
            }
            stop = state.run(story);
            next_scene = true;
        }
        durations.push((crate::now() - frame_started) * 1000.);
        frames += 1;
        if frames % 60 == 0 {
            save(
                "SKIP-PROGRESS",
                &serde_json::json!({"frames":frames,"dialogues":dialogues,"elapsed":crate::now()-began,"loads":renderer.stats().0-before.0}),
            );
        }
    }
    durations.sort_by(|a, b| a.partial_cmp(b).unwrap());
    let after = renderer.stats();
    let load_after = renderer.load_stats();
    save(
        "SKIP-METRICS",
        &serde_json::json!({"frames":frames,"dialogues":dialogues,"mean_ms":(crate::now()-began)*1000./frames as f64,"p95_ms":durations[durations.len()*95/100],"loads":after.0-before.0}),
    );
    assert!(
        (crate::now() - began) * 1000. / (frames as f64) < 40.,
        "Skip stalls rendering"
    );
    assert!(
        durations[durations.len() * 95 / 100] < 60.,
        "Skip has sustained slow frames"
    );
    assert_eq!(dialogues, 120);
    assert!(!gate.update(&mut latched, true, false, true, true));
    let pc = state.pc;
    for _ in 0..10 {
        assert!(!gate.update(&mut latched, true, false, false, true));
    }
    assert_eq!(pc, state.pc);
    renderer.scene(&state, story);
    renderer.dialogue(&state, story, "", usize::MAX);
    screenshot(renderer, "PSP-AFTER-SKIP");
    serde_json::json!({"dialogues":dialogues,"frames":frames,"elapsed_seconds":crate::now()-began,"mean_frame_ms":(crate::now()-began)*1000./frames as f64,"cancel_immediate":true,"unread_requires_release":true,"texture_loads":after.0-before.0,"scene_renders":after.1-before.1,"prefix_renders":load_after.2-load_before.2,"load_ms":load_after.0-load_before.0,"inflate_ms":load_after.1-load_before.1,"frame_p95_ms":durations[durations.len()*95/100],"frame_max_ms":durations[durations.len()-1]})
}
