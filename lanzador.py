#!/usr/bin/env python3
"""
Lanzador - punto de entrada del sistema de procesamiento de señales
"""

from senial_solid.lector_senial import LectorSenial


class Lanzador:
    """Orquesta la ejecución del pipeline: leer, procesar y mostrar la señal."""

    @staticmethod
    def ejecutar() -> None:
        """Ejecuta el pipeline completo sobre una señal de 10 muestras"""
        senial = LectorSenial(10)

        senial.leer_senial()
        senial.procesar_senial()
        senial.mostrar_senial()


def ejecutar() -> None:
    """Punto de entrada para el comando de consola (ver setup.py)"""
    Lanzador.ejecutar()


if __name__ == "__main__":
    ejecutar()
