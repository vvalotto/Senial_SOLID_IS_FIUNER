"""
Paquete lanzador - Orquestador principal del sistema

Contiene Lanzador, que coordina el flujo entre adquisicion_senial,
procesamiento_senial y presentacion_senial. Incluye crear_procesador(),
Factory que centraliza la decisión de qué procesador concreto crear.

Versión: 1.4.0
Autor: Victor Valotto
"""

from .lanzador import Lanzador, ejecutar

__version__ = "1.4.0"
__author__ = "Victor Valotto"
__all__ = ['Lanzador', 'ejecutar']
