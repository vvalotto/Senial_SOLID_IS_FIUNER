"""
Paquete dominio_senial - Entidades del dominio

Contiene la entidad Senial, núcleo estable del sistema. No depende
de ningún otro paquete.

Versión: 1.2.0
Autor: Victor Valotto
"""

from .senial import Senial, SenialPila

__version__ = "1.2.0"
__author__ = "Victor Valotto"
__all__ = ['Senial', 'SenialPila']
