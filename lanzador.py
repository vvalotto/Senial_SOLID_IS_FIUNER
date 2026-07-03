#!/usr/bin/env python3
"""
Lanzador - punto de entrada del sistema de procesamiento de señales
"""

from senial_solid.adquisidor import Adquisidor
from senial_solid.procesador import Procesador
from senial_solid.visualizador import Visualizador


class Lanzador:
    """Orquesta la ejecución del pipeline: leer, procesar y mostrar la señal."""

    @staticmethod
    def ejecutar() -> None:
        """Ejecuta el pipeline completo sobre una señal de 10 muestras"""
        adquisidor = Adquisidor(10)
        procesador = Procesador()
        visualizador = Visualizador()

        adquisidor.leer_senial()
        senial_adquirida = adquisidor.obtener_senial_adquirida()

        procesador.procesar_senial(senial_adquirida)
        senial_procesada = procesador.obtener_senial_procesada()

        visualizador.mostrar_datos(senial_adquirida, "Señal original:")
        visualizador.mostrar_datos(senial_procesada, "Señal amplificada (x2):")


def ejecutar() -> None:
    """Punto de entrada para el comando de consola (ver setup.py)"""
    Lanzador.ejecutar()


if __name__ == "__main__":
    ejecutar()
