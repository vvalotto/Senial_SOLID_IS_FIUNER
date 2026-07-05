# Requerimientos

Registro de los requerimientos que disparan cada evolución del sistema, en el orden en que se plantean. Un requerimiento puede plantearse en una versión y resolverse recién en otra posterior — cuando eso pasa, se indica en el campo "Resuelto en".

---

## Requerimiento 1: Sistema de Procesamiento de Señales

El sistema debe implementar un procesador de señales digitales que permita:

1. **Captura de señales**: Simular el ingreso de una señal digital mediante la entrada de valores numéricos por consola, donde cada valor representa una muestra de la señal.
2. **Procesamiento**: Procesar la señal capturada aplicando una amplificación con factor de 2x a cada muestra de la señal original.
3. **Visualización**: Mostrar tanto la señal original como la señal amplificada de manera clara y organizada.

---

## Requerimiento 2: Procesamiento por umbral

El sistema debe implementar un procesador de señales digitales que permita:

1. **Procesamiento por umbral**: Procesar la señal aplicando un umbral configurado, donde cualquier valor de la señal que supere ese umbral se reemplaza por cero.

---

## Requerimiento 3: Adquisición desde archivo

El sistema debe implementar un adquisidor de señales digitales que permita:

1. **Lectura desde archivo**: Leer la señal desde un archivo de texto, en lugar de simular su ingreso por consola.

---

## Requerimiento 4: Señales con comportamiento de pila y cola

El sistema debe implementar una entidad de señal digital que permita:

1. **Comportamiento de cola**: Procesar los datos de la señal en el mismo orden en que se ingresaron (FIFO), para escenarios de procesamiento en tiempo real.
2. **Comportamiento de pila**: Procesar los datos de la señal en orden inverso al de ingreso (LIFO), donde el último dato ingresado es el primero en procesarse.

---

## Requerimiento 5: Persistencia de señales

El sistema debe implementar un mecanismo de persistencia de señales digitales que permita:

1. **Guardar señales**: Persistir en disco tanto la señal adquirida como la señal procesada.
2. **Recuperar señales**: Recuperar desde disco una señal previamente persistida.
3. **Dos estrategias de persistencia**: Soportar persistencia binaria (serialización con `pickle`) y persistencia en un formato de texto ad-hoc, mapeando campo a campo.

---

## Requerimiento 6: Auditoría y trazabilidad de operaciones sobre señales

El sistema debe implementar un mecanismo de supervisión de las operaciones sobre señales que permita:

1. **Auditoría**: Registrar quién hizo qué operación sobre una señal y cuándo.
2. **Trazabilidad**: Registrar la traza de un evento (incluyendo errores) ocurrido sobre una señal, con un mensaje descriptivo.

