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
| `V7.0.0-(NoISP)` | — | Completado |
| `V8.0.0-(ISP)` | ISP | Completado |
| `V9.0.0-(NoDIP)` | — | Completado |
| `V10.0.0-(DIP)` | DIP | Completado |

Los 5 principios SOLID quedaron aplicados de punta a punta con el cierre de `V10.0.0-(DIP)`.

## Paquetes del sistema

| Paquete | Responsabilidad |
|---|---|
| `dominio_senial` | `SenialBase` y sus implementaciones (`SenialLista`, `SenialPila`, `SenialCola`), `FuenteSenial` y `FactorySenial` — núcleo del dominio |
| `adquisicion_senial` | Adquisidores (consola, archivo, senoidal) y `FactoryAdquisidor` |
| `procesamiento_senial` | Procesadores (amplificación, umbral) y `FactoryProcesador` |
| `presentacion_senial` | Visualización de señales y fuentes de señal |
| `persistidor_senial` | Persistencia (Repository Pattern) y `FactoryContexto` |
| `supervisor` | Auditoría y trazabilidad |
| `configurador` | Lee `config.json` (`CargadorConfig`) y delega en los Factories especializados — DIP |
| `lanzador` | Orquestación pura, sin decisiones de configuración |

## Licencia

MIT — ver [LICENSE](LICENSE).
