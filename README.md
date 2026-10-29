# Starry Flowers — PSP / Rust

Port nativo en Rust para PSP, mantenido en la rama `main` de [Starry-Flowers-PSP](https://github.com/enzocipher/Starry-Flowers-PSP). La versión de PC está en [Starry-Flowers-but-in-Rust](https://github.com/enzocipher/Starry-Flowers-but-in-Rust).

El firmware está en `psp/`; el motor narrativo y el layout que utiliza se incluyen en `src/`. El `Cargo.toml` de la raíz compila solamente esa biblioteca para pruebas de host, sin Macroquad ni aplicación de PC. Todos los scripts se ejecutan desde la raíz de este repositorio, que tiene su propia carpeta local `assets/`.

## Ejecutar

- ISO: `psp/dist/StarryFlowers.iso`, para PPSSPP o una PSP con firmware compatible con homebrew e imágenes ISO.
- Homebrew: copiar `psp/dist/EBOOT.PBP` y la carpeta `psp/dist/DATA` a `PSP/GAME/StarryFlowers/` en la Memory Stick.
- Los guardados propios están en `PSP/SAVEDATA/STARRYFLOWERS`. No son los guardados de Ren'Py ni de Windows.

La ISO y el EBOOT incluyen `ICON0.PNG` (144×80) y `PIC1.PNG` (480×272), preparados a partir del logo y el fondo originales para mostrar el juego en PPSSPP y el menú de PSP.

La ISO incorpora un ejecutable MIPS PSP real y los recursos convertidos de tu copia de Starry Flowers 1.7.4. El juego no requiere Python ni Ren'Py al ejecutarse.

## Controles

| Control | Acción |
|---|---|
| Cruceta | Seleccionar opciones o accesorios |
| X | Completar texto, avanzar o confirmar |
| O / L | Retroceder un diálogo; O vuelve en los menús |
| R mantenido | Saltar texto leído |
| Select | Activar/desactivar salto |
| Cuadrado | Activar/desactivar avance automático |
| Triángulo | Ocultar/mostrar diálogo |
| Start | Menú, ajustes y seis ranuras de guardado |
| Cuadrado / Triángulo en accesorios | Guardar/cargar accesorios favoritos |

Idioma inicial inglés; español seleccionable en Settings. Ajustes de velocidad de texto, avance automático, volúmenes separados, silenciar todo y comportamiento del salto. Los ajustes usan barras de flores y controles originales, agrupados para la pantalla de PSP. Se incluyen ambos recorridos iniciales, los capítulos, epílogo y ocho extras, además de una galería disponible al terminar.

## Compilar en Windows

Requiere Rust nightly con `rust-src`, `cargo-psp 0.2.9`, Python y los recursos originales en `../assets`. Se ha compilado con nightly de **2026-10-05**, host Windows GNU. Las versiones de Pillow, imageio-ffmpeg y pycdlib usadas por la preparación y el empaquetado están fijadas en `tools/requirements-psp.txt`.

```powershell
rustup toolchain install nightly-x86_64-pc-windows-gnu --component rust-src --profile minimal
cargo install cargo-psp --version 0.2.9
python -m pip install -r tools/requirements-psp.txt
# Desde la raíz del repositorio:
./tools/build_psp.ps1 -Python python
```

`prepare_psp.py` conserva el arte fuente y lo convierte en mosaicos PSP GE DXT5 con mipmaps; mantiene la geometría lógica del juego a escala 0,375, genera atlas de Nunito y convierte el audio a PCM estéreo de 44,1 kHz. La caché usa hashes de contenido y configuración para reutilizar imágenes y audio sin cambios. El manifiesto se valida antes de retirar archivos generados obsoletos que pertenecían al manifiesto anterior; los archivos desconocidos se conservan. `package_psp.py` genera la ISO y comprueba que `PSP_GAME/SYSDIR/EBOOT.BIN` contenga el ejecutable ELF nativo. Los archivos generados y los recursos del juego están excluidos de Git.

Desde la raíz del repositorio, ejecuta la preparación manual o las pruebas del pipeline así:

```powershell
python tools/prepare_psp.py
python -m unittest discover -s tools -p 'test_psp*.py'
```

La segunda preparación reutiliza los recursos cuyo contenido y receta no cambiaron. Para probar los bloques de audio en el host sin compilar el firmware PSP:

```powershell
$audioTest = Join-Path $env:TEMP 'starryflowers-audio-block-tests.exe'
rustc --test psp/src/audio_blocks.rs -o $audioTest
& $audioTest
```

## Memoria y SDK

Se compila la copia del motor narrativo incluida en este repositorio, adaptando sus colecciones a `alloc::collections::BTreeMap`. El ejecutable usa `no_std`, el SDK de PSP para archivos, mandos, pantalla y audio, un área de memoria de 18 MiB y una caché de texturas de 6 MiB que cuenta el próximo mosaico antes de cargarlo. Tres superficies alineadas de 1 MiB conservan el fondo, la escena y la escena anterior durante las transiciones; los atlas más usados permanecen en la caché. Se solicitan 333 MHz de CPU y 166 MHz de bus dentro de los límites del SDK; esto prioriza rendimiento sobre autonomía.

`third_party/psp` procede de `psp 0.3.14` (licencia MIT incluida). Su asignador original creaba un objeto del kernel por cada asignación; el guion agotaba el límite de objetos al cargar. El parche utiliza `linked_list_allocator` dentro de una sola reserva. Los trabajadores de audio no asignan memoria durante la reproducción. Los guardados se escriben primero en un archivo temporal y conservan un respaldo durante el reemplazo.

La revisión del 29 de octubre de 2026 valida los índices de accesorios, favoritos, pila y posición antes de cargar partidas; también comprueba un respaldo cuando el JSON principal es legible pero su estado es inválido. Normaliza ajustes y limita los reintentos de escritura automática a dos segundos. La música reintenta aperturas y errores de lectura con una espera de 500 ms; los errores repetidos de salida vuelven a reservar el canal. El EOF normal de efectos no dispara repeticiones.

Los glifos y las imágenes comparten sus nombres de archivo mediante `Arc<str>`, evitando asignar otra cadena por glifo y por copia de escena. La preparación v11 conserva la resolución fuente y comprueba los tres niveles de cada mosaico: si DXT5 supera el umbral de error, guarda su cadena completa en RGBA. En los recursos actuales son 5 de 2.567 mosaicos y 149.184 bytes adicionales. El verificador compara 7.701 niveles con el arte original y los 2.600 recursos de la ISO con los archivos preparados.

## Verificación y límites

`python tools/package_psp.py --audit` genera una ISO independiente para pruebas automáticas. Esta arranca en PPSSPP, captura el menú y el primer diálogo, recorre las dos rutas y los ocho extras, comprueba guardar/cargar y sobrescribir ajustes, y registra bloques de audio reproducidos. El resultado se escribe en `PSP/SAVEDATA/STARRYFLOWERS/AUDIT.JSON`. La ISO normal no activa esta prueba. `python tools/package_psp.py --performance-audit` permite ejecutar la comparación visual de ajustes, 120 cuadros de navegación, la transición de arranque y 120 diálogos con salto y renderizado real. Se verifica que navegar y animar la transición no carguen texturas ni reconstruyan escenas. Las pantallas de guardar/cargar leen las partidas una vez al entrar y actualizan la lista después de guardar.

El renderizador alterna dos búferes de pantalla y utiliza un tercer búfer reservado al componer transiciones, sin escribir sobre el que se está mostrando. Fuera de las mezclas dibuja las texturas a resolución fuente directamente, conservando el detalle al escalar en PPSSPP. Cada transición comprueba el diálogo de origen: una pantalla de ajustes no puede actuar como la escena anterior del juego. Un diálogo con los mismos gráficos actualiza su origen sin reconstruir la caché ni repetir una transición antigua. Cancelar skip tampoco reinicia los efectos omitidos. El ajuste de líneas usa avances de glifos y una caché limitada a 16 entradas. La caché de texturas mantiene su límite de 6 MiB, conserva el atlas de nombres y escribe a memoria solamente la textura recién cargada.

Las pruebas incluyen 12 vueltas entre ajustes y juego en inglés/español, comparando imágenes, y transiciones entre escenas vacías, a mitad de mezcla y entre diálogos con gráficos idénticos. Las capturas usan memoria alineada a 16 bytes para las transferencias GE. Para repetir las pruebas con una instalación de PPSSPP, después de compilar:

```powershell
./tools/test_psp.ps1 -Emulator 'C:/ruta/PPSSPPWindows64.exe' -Mode performance
./tools/test_psp.ps1 -Emulator 'C:/ruta/PPSSPPWindows64.exe' -Mode full -Resolution 3
./tools/test_psp.ps1 -Emulator 'C:/ruta/PPSSPPWindows64.exe' -Backend opengl
```

El script copia el emulador a un entorno de prueba dentro de `psp/test-emulator/runs`, con perfil PSP-1000 de 32 MiB, sin usar partidas personales. Guarda informes en `psp/dist` y termina solamente la instancia que inició. Se pueden indicar `-Python` y `-TimeoutSeconds` cuando haga falta. Las cargas de recursos al cambiar de escena todavía pueden producir cuadros más lentos que la navegación o los diálogos ya cargados.

Se prueba con el perfil PSP-1000 de 32 MiB de PPSSPP. La verificación en emulador no sustituye las pruebas en una PSP física. El renderizado utiliza la GPU de PSP, filtrado bilineal y mipmaps, transparencias y una caché de escenas en RAM a la resolución nativa de 480×272, evitando los alias de framebuffer que producían glitches en PPSSPP. Las fuentes y los controles se dibujan encima con los atlas originales a cuatro veces su tamaño. Los recursos originales de Windows se conservan; PSP utiliza arte adaptado a su resolución, audio estéreo, inglés/español y retroceso limitado a 32 diálogos; las animaciones de escena y la presentación de créditos son simplificadas. No tiene todavía todas las opciones visuales y de idiomas de Windows.

Historia, arte y música originales: **NomnomNami**. Tema final “Pretty in Pink”: **Marlene Bellissimo**. Se conserva la autoría y licencia de los recursos originales.

Los corazones azul, rojo y marrón se verifican en sus diálogos originales. Los gráficos Twemoji son de Twitter y colaboradores (CC-BY 4.0); los archivos originales de atribución se conservan junto a los recursos preparados.

About está disponible desde el menú inicial y el menú durante la partida. Izquierda/derecha o X recorren los créditos completos; O vuelve. Se incluyen los autores de las 13 traducciones del original, aunque PSP permite jugar en inglés/español, además de las listas completas de pruebas, agradecimientos y mecenas. La licencia original de Ren'Py está en `DATA/RENPY.TXT`.

El salto avanza como máximo cada 80 ms. Cancelarlo y detenerse ante texto no leído bloquea R hasta soltarlo; no se repiten los efectos de cámara ni las transiciones durante el salto. Las marcas de lectura se guardan cada dos segundos o al salir de la partida, en lugar de escribir por cada diálogo. El fondo estable se conserva aparte del retrato y la caja de diálogo. Los atlas se vinculan una vez por grupo de glifos consecutivos. La prueba de salto exige menos de 40 ms de media y 60 ms en el percentil 95; los resultados están en verification.json.
