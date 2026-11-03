# Diagramas de estado

## 1. Una señal con capacidad acotada (`SenialPila` / `SenialCola`)

Estados derivados de `cantidad` frente a `tamanio` (`dominio_senial/senial.py`).

```mermaid
stateDiagram-v2
    [*] --> Vacia : crear(tamanio)

    Vacia --> Parcial : poner_valor
    Parcial --> Parcial : poner_valor [cantidad + 1 < tamanio]
    Parcial --> Llena : poner_valor [cantidad + 1 == tamanio]

    Llena --> Llena : poner_valor / imprime error, descarta el valor

    Llena --> Parcial : sacar_valor
    Parcial --> Parcial : sacar_valor [cantidad - 1 > 0]
    Parcial --> Vacia : sacar_valor [cantidad - 1 == 0]
    Vacia --> Vacia : sacar_valor / retorna None

    Parcial --> Vacia : limpiar
    Llena --> Vacia : limpiar
```

Con `tamanio = 1`, `Vacia` pasa directo a `Llena`.

## 2. Ciclo de vida de una señal dentro del pipeline

```mermaid
stateDiagram-v2
    [*] --> Creada : Configurador crea la señal (vacía)
    Creada --> Adquirida : leer_senial() / poner_valor por cada muestra
    Adquirida --> Identificada : asignar id y fecha_adquisicion
    Identificada --> Persistida : repositorio.guardar()
    Persistida --> Consumida : procesador.procesar() / sacar_valor hasta vaciar
    Persistida --> Recuperada : repositorio.obtener(id)
    Recuperada --> Visualizada : visualizador.mostrar_datos()
    Visualizada --> [*]
    Consumida --> [*]
```

## Notas

- En el diagrama 2, la señal original queda **vacía en memoria** después de procesar (estado `Consumida`); lo que se muestra al final es la copia recuperada de disco.
- La señal procesada recorre el mismo ciclo desde `Creada`, y se llena con `poner_valor` desde el procesador.
- El `Lanzador` asigna el `id` y la fecha **antes** de guardar, así que el estado `Identificada` es una condición previa de la persistencia.
