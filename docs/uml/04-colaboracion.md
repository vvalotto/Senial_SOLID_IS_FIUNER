# Diagrama de colaboración (comunicación en UML 2)

Mermaid no tiene un tipo de diagrama de comunicación. Se representa con un diagrama de objetos enlazados y **mensajes numerados**, que es la característica distintiva del diagrama de comunicación frente al de secuencia: se enfatiza la estructura de enlaces, no el eje temporal.

Escenario: guardar la señal adquirida y registrar auditoría y traza (misma situación que el diagrama de secuencia 2).

```mermaid
flowchart LR
    L(["lanzador : Lanzador"])
    A(["adq : AdquisidorArchivo"])
    S(["senial : SenialLista"])
    R(["repo : RepositorioSenial"])
    X(["ctx : ContextoPickle"])
    LOG[("auditor.log<br/>logger.log")]

    L -- "1: leer_senial()" --> A
    A -- "1.1*: poner_valor(v)" --> S
    L -- "2: obtener_senial_adquirida()" --> A
    L -- "3: guardar(senial)" --> R
    R -- "3.1: persistir(senial, id)" --> X
    L -- "4: auditar(senial, msg)" --> R
    R -- "4.1: append" --> LOG
    L -- "5: trazar(senial, accion, msg)" --> R
    R -- "5.1: append" --> LOG
    A -. "enlace: _senial" .- S
    R -. "enlace: _contexto" .- X
```

## Lectura

- `1.1*` indica iteración: se repite por cada muestra.
- Los enlaces punteados son relaciones de la estructura (el adquisidor conoce su señal; el repositorio conoce su contexto). Los inyecta el `Configurador`.
- La numeración decimal (`3`, `3.1`) expresa anidamiento: `3.1` ocurre dentro de la ejecución de `3`.
