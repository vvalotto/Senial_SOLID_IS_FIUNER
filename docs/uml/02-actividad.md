# Diagrama de actividad

Flujo de `Lanzador.ejecutar()` (`lanzador/lanzador.py`).

```mermaid
flowchart TD
    inicio(("●")) --> cfg["Inicializar configuración<br/>(lee config.json)"]
    cfg --> vis["Crear visualizador"]
    vis --> in1[/"Ingresar nombre y descripción<br/>de la fuente"/]
    in1 --> fuente["Crear FuenteSenial y asignarle id"]
    fuente --> gfuente["Guardar fuente"]
    gfuente --> adq["Crear adquisidor<br/>y repositorio de adquisición"]
    adq --> leer["Leer señal<br/>(consola, archivo o senoidal)"]
    leer --> ida["Asignar id y fecha de adquisición"]
    ida --> gadq["Guardar señal adquirida"]
    gadq --> aud1["Auditar y trazar<br/>ADQUISICION"]
    aud1 --> proc["Crear procesador"]
    proc --> tipo{"¿Tipo de<br/>procesador?"}
    tipo -- amplificador --> amp["Multiplicar cada muestra<br/>por el factor"]
    tipo -- umbral --> umb["Reemplazar por 0 las muestras<br/>que superan el umbral"]
    amp --> idp["Asignar id y fecha<br/>a la señal procesada"]
    umb --> idp
    idp --> gproc["Guardar señal procesada"]
    gproc --> aud2["Auditar y trazar<br/>PROCESAMIENTO"]
    aud2 --> rec["Recuperar fuente,<br/>señal adquirida y señal procesada"]
    rec --> mostrar[/"Mostrar las tres entidades<br/>por consola"/]
    mostrar --> fin((("◉")))
```

## Notas

- El procesador drena la señal de entrada (`sacar_valor` hasta que `cantidad` es 0). Por eso la señal adquirida se guarda **antes** de procesar, y la que se muestra al final es la recuperada de disco.
- Con el adquisidor `consola` hay una iteración extra por muestra (leer y validar); con `archivo` se ignoran las líneas que no son números.
