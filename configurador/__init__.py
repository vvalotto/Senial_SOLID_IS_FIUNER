"""
Paquete configurador - Factory centralizado

Contiene Configurador, responsable de crear y configurar todas las
instancias que necesita la aplicación: adquisidor, procesador y
visualizador. Depende de adquisicion_senial, procesamiento_senial y
presentacion_senial.

Versión: 1.0.0
Autor: Victor Valotto
"""

from .configurador import Configurador

__version__ = "1.0.0"
__author__ = "Victor Valotto"
__all__ = ['Configurador']
