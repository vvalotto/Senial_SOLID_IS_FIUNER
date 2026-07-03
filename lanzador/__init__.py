"""
Paquete lanzador - Orquestador principal del sistema

Contiene Lanzador, que coordina el flujo entre adquisicion_senial,
procesamiento_senial y presentacion_senial.

Versión: 1.2.0
Autor: Victor Valotto
"""

from .lanzador import Lanzador, ejecutar

__version__ = "1.2.0"
__author__ = "Victor Valotto"
__all__ = ['Lanzador', 'ejecutar']
