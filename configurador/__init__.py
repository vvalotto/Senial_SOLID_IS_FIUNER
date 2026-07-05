"""
Paquete configurador - Factory centralizado

Contiene Configurador, responsable de crear y configurar todas las
instancias que necesita la aplicación: adquisidor, procesador,
visualizador, contexto de persistencia y repositorio. Depende de
adquisicion_senial, procesamiento_senial, presentacion_senial y
persistidor_senial.

Versión: 2.0.0
Autor: Victor Valotto
"""

from .configurador import Configurador

__version__ = "2.0.0"
__author__ = "Victor Valotto"
__all__ = ['Configurador']
