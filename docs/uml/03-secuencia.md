# Diagramas de secuencia

## 1. Creación de dependencias (DIP)

Qué pasa cuando el `Lanzador` pide un adquisidor. Él no conoce ningún tipo concreto: lo resuelve el `Configurador` con config.json y los factories.

```mermaid
sequenceDiagram
    participant L as Lanzador
    participant C as Configurador
    participant CC as CargadorConfig
    participant FS as FactorySenial
    participant FA as FactoryAdquisidor

    L->>C: inicializar_configuracion()
    C->>CC: cargar()
    CC-->>C: config (dict)

    L->>C: crear_adquisidor()
    C->>CC: obtener_config_adquisidor()
    CC-->>C: {tipo: archivo, ruta_archivo: ...}
    C->>CC: obtener_config_senial_adquisidor()
    CC-->>C: {tipo: lista, tamanio: 10}
    C->>FS: crear("lista", config)
    FS-->>C: SenialLista
    C->>FA: crear("archivo", config, senial)
    FA-->>C: AdquisidorArchivo
    C-->>L: BaseAdquisidor
```

## 2. Adquisición y persistencia de la señal

Primera mitad del pipeline: leer, guardar, auditar y trazar.

```mermaid
sequenceDiagram
    participant L as Lanzador
    participant A as BaseAdquisidor
    participant S as SenialBase
    participant R as RepositorioSenial
    participant X as ContextoPickle
    participant F as Archivos de log

    L->>A: leer_senial()
    loop por cada muestra
        A->>S: poner_valor(valor)
    end
    L->>A: obtener_senial_adquirida()
    A-->>L: senial
    L->>S: id = hash, fecha_adquisicion = hoy
    L->>R: guardar(senial)
    R->>X: persistir(senial, id)
    X->>X: pickle.dump → id.pickle
    L->>R: auditar(senial, mensaje)
    R->>F: append en auditor.log
    L->>R: trazar(senial, "ADQUISICION", mensaje)
    R->>F: append en logger.log
```

## 3. Procesamiento y recuperación

Segunda mitad: procesar, guardar y volver a leer de disco para mostrar.

```mermaid
sequenceDiagram
    participant L as Lanzador
    participant P as BaseProcesador
    participant SA as Señal adquirida
    participant SP as Señal procesada
    participant R as RepositorioSenial
    participant V as Visualizador

    L->>P: procesar(senial_adquirida)
    loop mientras cantidad > 0
        P->>SA: sacar_valor()
        SA-->>P: valor
        P->>SP: poner_valor(f(valor))
    end
    L->>P: obtener_senial_procesada()
    P-->>L: senial_procesada
    L->>R: guardar(senial_procesada)
    L->>R: auditar(...) y trazar("PROCESAMIENTO", ...)
    L->>R: obtener(id_adquirida)
    R-->>L: señal adquirida recuperada
    L->>R: obtener(id_procesada)
    R-->>L: señal procesada recuperada
    L->>V: mostrar_datos(recuperada, titulo)
```
