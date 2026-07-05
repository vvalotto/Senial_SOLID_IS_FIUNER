# Configuraciones de ejemplo

Seis variantes de `config.json` para probar distintas combinaciones sin tocar
ningún archivo `.py` — la prueba de DIP está en el uso, no en el diseño.

No están cableadas automáticamente (no hay selección por argumento ni
variable de entorno). Para probar una, copiala sobre `configurador/config.json`:

```bash
cp configurador/ejemplos/config-02-pila-senoidal-umbral.json configurador/config.json
python -m lanzador.lanzador
```

Ninguna usa `adquisidor.tipo = "consola"` (requiere ingresar valores a mano);
todas combinan `archivo` o `senoidal` para poder ejecutarse de punta a punta
sin intervención manual de datos.

| Archivo | Señal adq./proc. | Adquisidor | Procesador | Contextos |
|---|---|---|---|---|
| `config-01-lista-archivo-amplificador.json` | lista / lista | archivo | amplificador (3.0) | pickle / pickle / pickle |
| `config-02-pila-senoidal-umbral.json` | pila / pila | senoidal | umbral (5) | archivo / archivo / archivo |
| `config-03-cola-senoidal-amplificador-mixto.json` | cola / lista | senoidal | amplificador (1.5) | pickle / archivo / pickle |
| `config-04-lista-cola-archivo-umbral.json` | lista / cola | archivo | umbral (6) | archivo / pickle / archivo |
| `config-05-pila-senoidal-amplificador.json` | pila / pila | senoidal | amplificador (0.5) | pickle / pickle / archivo |
| `config-06-cola-archivo-umbral-mixto.json` | cola / lista | archivo | umbral (4) | archivo / archivo / pickle |
