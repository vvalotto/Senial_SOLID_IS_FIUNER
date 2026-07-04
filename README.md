# Senial SOLID — FIUNER

Caso de estudio didáctico: un sistema de procesamiento de señales digitales en Python que evoluciona, principio por principio, desde violaciones deliberadas de SOLID hasta una arquitectura que los aplica correctamente.

## Cómo se navega

El historial de commits está diseñado para leerse, no solo para acumularse. Cada versión importante tiene un tag. Los tags marcan un estado del sistema que es completo y ejecutable — podés hacer `git checkout` de cualquiera y correr el sistema tal como estaba en ese punto de la evolución.

```bash
git clone https://github.com/vvalotto/Senial_SOLID_IS_FIUNER.git
cd Senial_SOLID_IS_FIUNER
git tag -l
git checkout V1.0.0-(NoSRP)
```

La convención de numeración: cada principio corregido abre una versión mayor nueva (`V2.0.0`, `V3.0.0`, `V4.0.0`...). Las violaciones y variantes intermedias de un mismo principio son versiones menores del entero anterior (`V2.1.0`, `V4.1.0`, `V5.3.0`...).

## Hoja de ruta de versiones

| Tag | Principio | Estado |
|---|---|---|
| `V1.0.0-(NoSRP)` | — | Completado |
| `V2.0.0-(SRP)` | SRP (clases) | Completado |
| `V2.1.0-(SRP-Paquetes)` | SRP (paquetes) | Completado |
| `V3.0.0-(NoOCP)` | — | Completado |
| `V4.0.0-(OCP)` | OCP | Completado |
| `V5.0.0-(NoLSP)` | — | Completado |
| `V6.0.0-(LSP)` | LSP | Completado |
| `V6.3.0-(NoISP)` | — | Pendiente de definir |
| `V7.0.0-(ISP)` | ISP | Pendiente de definir |
| `V7.x-(NoDIP)` | — | Pendiente de definir |
| `V8.0.0-(DIP)` | DIP | Pendiente de definir |

"Planificado" significa que la ficha de migración (requerimiento simulado, objetivo de aprendizaje, progresión de commits) ya está validada; el código todavía no se escribió en este repo.

## Paquetes del sistema

| Paquete | Responsabilidad |
|---|---|
| `dominio_senial` | `SenialBase` y sus implementaciones (`SenialLista`, `SenialPila`, `SenialCola`) — núcleo del dominio |
| `adquisicion_senial` | Adquisidores (consola, archivo) |
| `procesamiento_senial` | Procesadores (amplificación, umbral, pipeline) |
| `presentacion_senial` | Visualización |
| `persistidor_senial` | Persistencia (Repository Pattern) |
| `supervisor` | Auditoría y trazabilidad |
| `configurador` | Factory centralizado |
| `lanzador` | Orquestación |

## Licencia

MIT — ver [LICENSE](LICENSE).
