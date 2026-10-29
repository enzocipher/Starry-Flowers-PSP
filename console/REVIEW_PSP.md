# Revisión PSP — 29 de octubre de 2026

La rama `dev-psp` compila y supera las comprobaciones locales descritas abajo. Se corrigieron fallos de guardado, recuperación de audio, empaquetado y calidad de mipmaps; se redujo la creación de cadenas durante el renderizado. La prueba de salto mejora en esta ejecución de PPSSPP, aunque siguen los picos al cargar recursos. No se ha probado una PSP física.

Base: `7ebfb2bd3296594196c3e43989150a8851d620f0`, igual a la rama remota consultada durante la revisión. Se incluyeron y conservaron los cambios locales que ya existían; este informe distingue las mejoras de esta sesión. No se crearon commits ni se publicó contenido.

## Correcciones aplicadas

| Prioridad | Problema observado | Resultado |
|---|---|---|
| P1 | Un SLOT con `acc` o `fave` fuera de rango podía llegar al indexado del renderizador y provocar un panic. | Se validan accesorios, favoritos, pila, posición y operación reanudable antes de aceptar el estado. Un respaldo válido se considera también cuando el JSON principal deserializa pero es inválido semánticamente. |
| P2 | Una apertura o lectura fallida dejaba la música sin nueva apertura; tres errores de salida terminaban el trabajador. | Reintentos de música cada 500 ms y nueva reserva del canal tras errores de salida. Los efectos terminados y los bucles vacíos no se reinician. |
| P2 | Una escritura automática fallida podía repetirse cada cuadro. El resultado del cierre se ignoraba. | Los intentos periódicos quedan separados por dos segundos, con un intento inmediato al salir del juego; el temporal se promueve solo tras escritura y cierre satisfactorios. |
| P2 | El empaquetado omitía silenciosamente recursos ausentes; el verificador no comparaba los recursos de DATA en la ISO. | Se validan la lista completa y sus referencias antes de escribir el paquete; se compara SHA-256 de cada recurso empaquetado. |
| P2 | Se comprobaba calidad solo en el nivel base. Se encontraron seis niveles con error superior al umbral, en cinco mosaicos. | La receta v11 conserva toda la cadena de esos mosaicos en RGBA sin pérdida. Son 5/2.567 mosaicos y 149.184 bytes adicionales. |
| P2 | La CI invocaba una biblioteca y una feature inexistentes. | Se exponen motor/layout como biblioteca y se define `original-assets`; la CI también prueba audio, skip y persistencia. |
| P2 | El script podía perder la carrera entre `Test-Path` y `Get-Item` mientras el guardado renombraba PERF.JSON. | Consulta única de metadatos tolerante al intervalo del reemplazo. La ejecución posterior finalizó correctamente. |

En renderizado, `Draw`, `Tile` y `Glyph` comparten los nombres mediante `Arc<str>`, incluidas las copias de escenas. Las marcas de lectura permanecen ordenadas y se consultan con búsqueda binaria. Se activa el borrado rápido del SDK y se solicitan 333 MHz de CPU / 166 MHz de bus. Se mantiene la caché de texturas de **6 MiB que ya tenía el código local**, el heap de 18 MiB y el arte a resolución fuente. Las capturas RAM a 480×272 se usan para las mezclas; no sustituyen el detalle fuente del renderizado normal.

## Evidencia

- Build PSP incremental con nightly instalado `1.101.0-nightly (282215592 2026-10-04)`: salida 0, PRX y EBOOT generados.
- `cargo test --locked`: 11 pruebas de biblioteca y 22 del ejecutable aprobadas; 1 benchmark manual ignorado. Los tests comunes aparecen en ambos destinos. `cargo test --lib --locked --no-default-features`: 11 aprobadas, sin recursos originales.
- Helpers PSP en host: 7 de audio, 4 de skip y 3 de persistencia aprobadas. Python: 18 aprobadas.
- PPSSPP 1.20.4, perfil PSP-1000 / 32 MiB: auditoría completa final Vulkan 3x aprobada; 4.781 diálogos, dos finales, ocho extras, tres símbolos y 1.070 bloques de música. Incluye guardados inválidos, respaldo semántico, normalización y apertura de audio que falla y luego se recupera.
- Auditorías de rendimiento finales Vulkan 1x y OpenGL 1x aprobadas. Doce regresos ajustes/juego sin contaminación visual; navegación de ajustes sin nuevas cargas de texturas ni reconstrucciones de escena.
- Tres capturas estáticas Vulkan 1x comparadas con la línea base: ajustes, primer diálogo y diálogo tras skip. **Cero píxeles RGB diferentes** en las tres; no implica igualdad de todas las escenas.
- Verificador final: 2.567 mosaicos, **7.701 niveles**, 2.600 recursos ISO y ejecutables ISO/PBP comprobados. Peor error medio premultiplicado entre niveles DXT5 restantes: **11,883/255**. Los cinco mosaicos RGBA coinciden exactamente con sus fuentes preparadas en todos sus niveles.
- Preparación incremental v11: 465/465 imágenes y 15/15 audios reutilizados; cero archivos obsoletos en la segunda ejecución. DATA: aproximadamente 297,0 MiB; ISO: 301,1 MiB.

Comparación de la misma auditoría de 120 diálogos con Vulkan 1x:

| Medida | Antes | Después |
|---|---:|---:|
| Media de cuadro | 19,925 ms | 19,114 ms |
| Percentil 95 | 20,865 ms | 16,729 ms |
| Máximo | 183,538 ms | 183,486 ms |
| Cargas de textura | 272 | 272 |
| Navegación de ajustes | 16,683 ms | 16,683 ms |

Es una medición por variante en emulador, con vsync y el mismo recorrido; no establece una mejora general de FPS ni una velocidad equivalente en hardware. Las optimizaciones no eliminan el pico de lectura de recursos.

Los informes completos y la comparación visual están en `psp/dist/full-vulkan-3x.json`, `performance-vulkan-1x.json`, `performance-opengl-1x.json`, `review-visual-comparison.json` y `review-comparison.png`. `psp/verification.json` registra los resultados y los hashes de los paquetes normales.

## Respecto a PC y trabajo pendiente

Se conserva el motor narrativo compartido y las rutas verificadas. PSP mantiene inglés/español, rollback de 32 diálogos frente a 250 en PC y animaciones/créditos simplificados. La revisión no implementa los demás idiomas ni todas las opciones visuales de PC.

Quedan por medir en PSP física la fluidez, autonomía a 333 MHz, suspensión/reanudación, escucha de bucles y recuperación de errores reales de lectura/salida. La recuperación de apertura se probó en emulador; no se inyectaron fallos de `sceAudioOutputBlocking` ni errores de cierre de Memory Stick. El siguiente trabajo de rendimiento debe centrarse en las cargas de escena y el coste de DXT5, con perfiles de hardware antes de cambiar formatos globalmente o aumentar memoria.

## Método y referencias

Se leyó `playstation-sdk` y las skills console de revisión, gráficos, audio, guardados, empaquetado y pruebas. `playstation-sdk` contiene solo una orientación mínima; las herramientas console son de PS2Recomp y no aportan validación específica de PSP. Se aplicó su método de builds incrementales, A/B, límites de memoria y evidencia de ejecución al proyecto nativo PSP. Copilot CLI, con su configuración predeterminada y sin aprobaciones automáticas, propuso cambios mecánicos y pruebas; sus propuestas se revisaron y corrigieron antes de aplicarlas.

La elección de reloj respeta los [límites documentados por PSPSDK](https://pspdev.github.io/pspsdk/psppower_8h.html). Las futuras optimizaciones deben tener en cuenta el [comportamiento de la caché de texturas medido por PPSSPP en PSP](https://www.ppsspp.org/docs/psp-hardware/gpu/texture-cache/) y sus [notas de rendimiento del GE](https://www.ppsspp.org/docs/development/psp-internals/ge-performance/).

## Migración del repositorio

La revisión anterior se realizó antes de la separación. Desde el 29 de octubre de 2026 este informe, el firmware, el SDK y los scripts se mantienen en `enzocipher/Starry-Flowers-PSP`, rama `main`. El motor narrativo y el layout se incluyen aquí; la aplicación Macroquad de PC continúa en `enzocipher/Starry-Flowers-but-in-Rust`. La separación conserva las fuentes de ejecución PSP y no introduce cambios de comportamiento.
