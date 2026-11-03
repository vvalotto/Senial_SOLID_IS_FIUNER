# Diagrama de paquetes

Dependencias reales entre paquetes, derivadas de los `import` del código (estado `main`, V10 DIP).
Una flecha `A --> B` significa "A importa de B".

```mermaid
flowchart TD
    subgraph entrada["Orquestación"]
        lanzador["«package»<br/>lanzador"]
        configurador["«package»<br/>configurador"]
    end

    subgraph funcional["Funcionalidad"]
        adquisicion["«package»<br/>adquisicion_senial"]
        procesamiento["«package»<br/>procesamiento_senial"]
        presentacion["«package»<br/>presentacion_senial"]
        persistidor["«package»<br/>persistidor_senial"]
    end

    subgraph nucleo["Núcleo estable"]
        dominio["«package»<br/>dominio_senial"]
        supervisor["«package»<br/>supervisor"]
    end

    lanzador --> configurador
    lanzador --> dominio
    configurador --> dominio
    configurador --> adquisicion
    configurador --> procesamiento
    configurador --> presentacion
    configurador --> persistidor
    presentacion --> dominio
    persistidor --> supervisor
```

## Qué mostrar en clase

- `dominio_senial` y `supervisor` no dependen de nadie: son el núcleo estable.
- `adquisicion_senial` y `procesamiento_senial` tampoco dependen de nadie; solo `configurador` los conoce.
- `lanzador` no importa ningún paquete concreto de adquisición, procesamiento ni persistencia: eso es DIP.
- Todas las flechas apuntan hacia el núcleo (sin ciclos).
