# Diagramas UML del sistema

Diagramas del estado actual del sistema (`main`, V10 DIP), escritos en [Mermaid](https://mermaid.js.org/) para que GitHub los renderice directamente.

| # | Diagrama | Archivo |
|---|---|---|
| 1 | Paquetes | [01-paquetes.md](01-paquetes.md) |
| 2 | Actividad | [02-actividad.md](02-actividad.md) |
| 3 | Secuencia (3 diagramas) | [03-secuencia.md](03-secuencia.md) |
| 4 | Colaboración / comunicación | [04-colaboracion.md](04-colaboracion.md) |
| 5 | Despliegue | [05-despliegue.md](05-despliegue.md) |
| 6 | Estado (2 diagramas) | [06-estado.md](06-estado.md) |
| 7 | Componentes | [07-componentes.md](07-componentes.md) |

## Limitaciones de Mermaid

Mermaid soporta de forma nativa solo secuencia, estado y actividad (aproximada con `flowchart`). Los diagramas de paquetes, colaboración, despliegue y componentes usan `flowchart` con estereotipos UML escritos a mano (`«component»`, `«device»`, etc.). Si se necesita notación UML estricta, el siguiente paso sería PlantUML.
