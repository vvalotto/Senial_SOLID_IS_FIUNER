"""
Paquete dominio_senial - Entidades del dominio

Contiene la jerarquía de señales digitales, núcleo estable del sistema.
No depende de ningún otro paquete. SenialBase define el contrato común;
SenialLista, SenialPila y SenialCola son sus implementaciones concretas.

Versión: 3.0.0
Autor: Victor Valotto
"""

from .senial import SenialBase, SenialLista, SenialPila, SenialCola

__version__ = "3.0.0"
__author__ = "Victor Valotto"
__all__ = ['SenialBase', 'SenialLista', 'SenialPila', 'SenialCola']
