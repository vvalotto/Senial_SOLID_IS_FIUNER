"""
Paquete senial_solid - SRP aplicado a nivel de clase

LectorSenial se separó en cuatro clases con responsabilidad única:
Senial (entidad de dominio), Adquisidor (lectura), Procesador
(amplificación x2) y Visualizador (presentación).

Versión: 2.0.0
Autor: Victor Valotto
"""

from .senial import Senial
from .adquisidor import Adquisidor
from .procesador import Procesador
from .visualizador import Visualizador

__version__ = "2.0.0"
__author__ = "Victor Valotto"
__all__ = ['Senial', 'Adquisidor', 'Procesador', 'Visualizador']
