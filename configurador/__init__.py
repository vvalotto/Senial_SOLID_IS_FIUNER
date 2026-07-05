"""
Paquete configurador - Factory centralizado

Contiene Configurador, responsable de crear y configurar todas las
instancias que necesita la aplicación: adquisidor, procesador,
visualizador y persistidor. Depende de adquisicion_senial,
procesamiento_senial, presentacion_senial y persistidor_senial.

Versión: 1.2.0
Autor: Victor Valotto
"""

from .configurador import Configurador

__version__ = "1.2.0"
__author__ = "Victor Valotto"
__all__ = ['Configurador']
