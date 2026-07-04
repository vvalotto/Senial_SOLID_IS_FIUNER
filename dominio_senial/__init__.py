"""
Paquete dominio_senial - Entidades del dominio

Contiene la entidad Senial, núcleo estable del sistema. No depende
de ningún otro paquete.

Versión: 2.0.0
Autor: Victor Valotto
"""

from .senial import Senial, SenialPila, SenialCola

__version__ = "2.0.0"
__author__ = "Victor Valotto"
__all__ = ['Senial', 'SenialPila', 'SenialCola']
