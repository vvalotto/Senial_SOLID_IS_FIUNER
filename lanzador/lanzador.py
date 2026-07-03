#!/usr/bin/env python3
"""
Lanzador - punto de entrada del sistema de procesamiento de señales
"""

from adquisicion_senial import Adquisidor
from procesamiento_senial import Procesador, ProcesadorUmbral
from presentacion_senial import Visualizador


class Lanzador:
    """Orquesta la ejecución del pipeline: leer, procesar y mostrar la señal."""

    @staticmethod
    def ejecutar() -> None:
        """Ejecuta el pipeline completo sobre una señal de 10 muestras"""
        adquisidor = Adquisidor(10)
        visualizador = Visualizador()

        adquisidor.leer_senial()
        senial_adquirida = adquisidor.obtener_senial_adquirida()

        tipo_procesamiento = "umbral"
        parametro = 5.0

        if tipo_procesamiento == "amplificar":
            procesador = Procesador()                # constructor sin parámetros
            procesador.procesar_senial(senial_adquirida)
        elif tipo_procesamiento == "umbral":
            procesador = ProcesadorUmbral(parametro)  # constructor diferente
            procesador.procesar_senial(senial_adquirida)

        senial_procesada = procesador.obtener_senial_procesada()

        visualizador.mostrar_datos(senial_adquirida, "Señal original:")
        visualizador.mostrar_datos(senial_procesada, "Señal con umbral aplicado (umbral=5.0):")


def ejecutar() -> None:
    """Punto de entrada para el comando de consola (ver setup.py)"""
    Lanzador.ejecutar()


if __name__ == "__main__":
    ejecutar()
