# Diagrama de componentes

Cada paquete instalable (tiene su propio `setup.py`) es un componente. Se muestran las **interfaces provistas** (contratos abstractos) y las **requeridas**.

Mermaid no tiene diagrama de componentes nativo: se representa con subgrafos «component» e interfaces como nodos circulares.

```mermaid
flowchart LR
    subgraph lanz["«component» lanzador"]
        Lanzador["Lanzador"]
    end

    subgraph conf["«component» configurador"]
        Configurador["Configurador"]
        CargadorConfig["CargadorConfig"]
    end

    subgraph dom["«component» dominio_senial"]
        ISenial(("SenialBase"))
        FactorySenial["FactorySenial"]
        FuenteSenial["FuenteSenial"]
    end

    subgraph adq["«component» adquisicion_senial"]
        IAdq(("BaseAdquisidor"))
        FactoryAdq["FactoryAdquisidor"]
    end

    subgraph pro["«component» procesamiento_senial"]
        IPro(("BaseProcesador"))
        FactoryPro["FactoryProcesador"]
    end

    subgraph per["«component» persistidor_senial"]
        IRepo(("BaseRepositorio"))
        IContexto(("BaseContexto"))
        FactoryCtx["FactoryContexto"]
    end

    subgraph sup["«component» supervisor"]
        IAud(("BaseAuditor"))
        ITraz(("BaseTrazador"))
    end

    subgraph pre["«component» presentacion_senial"]
        Visualizador["Visualizador"]
    end

    Lanzador -- "requiere" --> Configurador
    Lanzador -- "requiere" --> FuenteSenial
    Configurador -- "usa" --> CargadorConfig
    Configurador -- "requiere" --> FactorySenial
    Configurador -- "requiere" --> FactoryAdq
    Configurador -- "requiere" --> FactoryPro
    Configurador -- "requiere" --> FactoryCtx
    Configurador -- "requiere" --> Visualizador

    FactorySenial -. "provee" .-> ISenial
    FactoryAdq -. "provee" .-> IAdq
    FactoryPro -. "provee" .-> IPro
    FactoryCtx -. "provee" .-> IContexto
    IRepo -- "requiere" --> IContexto
    IRepo -- "requiere" --> IAud
    IRepo -- "requiere" --> ITraz
    Visualizador -- "requiere" --> ISenial
```

## Qué mostrar en clase

- Las dependencias entre componentes pasan por **interfaces** (círculos), no por clases concretas: DIP.
- `persistidor_senial` requiere las dos interfaces pequeñas de `supervisor` (`BaseAuditor`, `BaseTrazador`) en lugar de una interfaz grande única: ISP.
- Agregar un tipo nuevo (por ejemplo un procesador) solo toca el componente que lo contiene y su factory: OCP.
- Solo `configurador` conoce a todos los demás componentes: es el punto único de ensamblado.
