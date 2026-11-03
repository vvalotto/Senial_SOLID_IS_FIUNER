# Diagrama de despliegue

El sistema es una aplicación local de un solo nodo. El diagrama muestra el ciclo completo: build en la máquina de desarrollo, release como artefactos, instalación y ejecución con los archivos que se generan.

```mermaid
flowchart LR
    subgraph dev["«device» Máquina de desarrollo"]
        subgraph repo["«artifact» Repositorio Git"]
            fuentes["8 paquetes + metapackage<br/>(código fuente y setup.py)"]
            buildsh["build/build_all.sh"]
        end
        subgraph rel["«artifact» packaging/release"]
            wheels["wheels (.whl)"]
            sdists["sdists (.tar.gz)"]
        end
        buildsh -- "python -m build" --> wheels
        buildsh -- "python -m build" --> sdists
        fuentes --> buildsh
    end

    subgraph usuario["«device» Máquina del usuario"]
        subgraph env["«execution environment» Python 3.8+ / venv senial_env"]
            inst["install/install.sh<br/>(pip install)"]
            subgraph app["«artifact» senial-solid-fiuner"]
                cmd["comando senial-solid-fiuner<br/>(lanzador.ejecutar)"]
                cfg["config.json"]
            end
        end
        subgraph disco["«artifact» Sistema de archivos"]
            entrada["senial.txt<br/>(entrada)"]
            datos["datos_persistidos/<br/>adquisicion, procesamiento,<br/>fuente_senial (.pickle)"]
            logs["auditor.log<br/>logger.log"]
        end
    end

    wheels -- "copia / instalación" --> inst
    inst --> app
    cmd -- "lee" --> cfg
    cmd -- "lee" --> entrada
    cmd -- "escribe" --> datos
    cmd -- "escribe" --> logs
```

## Notas

- No hay servidores, red ni base de datos: la «persistencia» es el sistema de archivos local.
- Los contextos de persistencia (`pickle` o `archivo`) y las rutas se eligen en `config.json`; el diagrama muestra la configuración por defecto.
- Los logs se escriben en el directorio desde el que se ejecuta el comando.
