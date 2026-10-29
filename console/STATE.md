# Starry Flowers — estado del port PSP

Actualizado: 29 de octubre de 2026. Port nativo Rust, rama `main` de `enzocipher/Starry-Flowers-PSP`; no utiliza PS2Recomp. Revisión y resultados en [REVIEW_PSP.md](REVIEW_PSP.md).

- Base Git: `7ebfb2bd3296594196c3e43989150a8851d620f0`; trabajo previo local conservado. Sin commit/push en esta sesión.
- Toolchain disponible: `nightly-x86_64-pc-windows-gnu`, rustc `1.101.0-nightly (282215592 2026-10-04)`.
- Heap: 18 MiB; caché de texturas: 6 MiB; CPU/bus solicitados: 333/166 MHz.
- Receta de imágenes: v11, resolución fuente, DXT5 con RGBA de respaldo por calidad de toda la cadena. Cinco mosaicos usan RGBA.
- Python de validación: `%TEMP%/starryflowers-psp-review-python/Scripts/python.exe`, entorno aislado con `tools/requirements-psp.txt`. El Python de MSYS en PATH no tenía Pillow.
- Emulador fuente: `psp/test-emulator/PPSSPPWindows64.exe`, v1.20.4. Perfiles de prueba aislados en `psp/test-emulator/runs`.
- ISO normal y EBOOT: `psp/dist/StarryFlowers.iso`, `psp/dist/EBOOT.PBP`. La ISO de auditoría es independiente.
- Copia previa de paquetes, capturas y diff inicial: `%TEMP%/starryflowers-psp-review-20261029-164359`.

## Comandos comprobados

Desde `psp/`, build incremental sin limpiar:

```powershell
cargo +nightly-x86_64-pc-windows-gnu psp --release --locked '-Zbuild-std=core,alloc,compiler_builtins,panic_unwind'
```

Desde la raíz:

```powershell
$taskPython = Join-Path $env:TEMP 'starryflowers-psp-review-python/Scripts/python.exe'
cargo test --locked
cargo test --lib --locked --no-default-features
& $taskPython -m unittest discover -s tools -p 'test_psp*.py'
& $taskPython tools/package_psp.py
& $taskPython tools/verify_psp_native.py
./tools/test_psp.ps1 -Emulator 'psp/test-emulator/PPSSPPWindows64.exe' -Python $taskPython -Mode full -Resolution 3
./tools/test_psp.ps1 -Emulator 'psp/test-emulator/PPSSPPWindows64.exe' -Python $taskPython -Mode performance
./tools/test_psp.ps1 -Emulator 'psp/test-emulator/PPSSPPWindows64.exe' -Python $taskPython -Mode performance -Backend opengl
```

Para cada helper `audio_blocks`, `playback`, `persistence`, se compiló `psp/src/<helper>.rs` con `rustc --edition=2021 --test` y se ejecutó su salida temporal. Los mismos comandos están en CI.

## Patrones y límites

- Validar estados antes de indexar accesorios, incluso cuando JSON deserializa. Aplicar el mismo predicado al respaldo.
- Registrar el momento del intento de guardado, aunque falle. Promover el temporal únicamente después de cerrar correctamente.
- No usar `Test-Path` seguido de `Get-Item` para observar un archivo que se reemplaza mediante renombrado.
- Medir todos los mipmaps: el nivel base puede pasar y un nivel reducido perder demasiado detalle.
- Comparar las salidas completas del paquete con el manifiesto; no iterar solo los archivos que casualmente existen.
- Mantener comandos de prueba secuenciales por emulador. No tocar las partidas personales.
- Las auditorías anteriores del 5/15 de octubre no certifican cambios nuevos. Los resultados de esta sesión reemplazan las métricas actuales en `psp/verification.json`.
- Pendientes: PSP física, suspensión, fallos reales de salida de audio/cierre y picos de carga de escenas. No se declara paridad total con PC.

## Separación de repositorios

El 29 de octubre de 2026 el firmware, SDK y herramientas de PSP se separaron del repositorio de PC. `src/engine.rs`, `src/layout.rs` y `story.json` son copias propias de este repositorio. La raíz se prueba como biblioteca `starryflowers-psp-core`; `psp/` conserva su crate independiente. No se requiere un checkout del repositorio de PC.
