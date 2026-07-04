"""
Paquete dominio_senial - Entidades del dominio

Contiene la jerarquía de señales digitales, núcleo estable del sistema.
No depende de ningún otro paquete. SenialBase define el contrato común;
SenialLista, SenialPila y SenialCola son sus implementaciones concretas.
El alias Senial (= SenialLista) se mantiene temporalmente por compatibilidad.

Versión: 2.1.0
Autor: Victor Valotto
"""

from .senial import Senial, SenialBase, SenialLista, SenialPila, SenialCola

__version__ = "2.1.0"
__author__ = "Victor Valotto"
__all__ = ['Senial', 'SenialBase', 'SenialLista', 'SenialPila', 'SenialCola']
