"""
Paquete dominio_senial - Entidades del dominio

Contiene la jerarquía de señales digitales, núcleo estable del sistema,
la entidad FuenteSenial (catálogo de orígenes de señal) y FactorySenial,
que crea señales a partir de un tipo y una configuración. No depende de
ningún otro paquete. SenialBase define el contrato común; SenialLista,
SenialPila y SenialCola son sus implementaciones concretas.

Versión: 3.2.0
Autor: Victor Valotto
"""

from .senial import SenialBase, SenialLista, SenialPila, SenialCola
from .fuente_senial import FuenteSenial
from .factory_senial import FactorySenial

__version__ = "3.2.0"
__author__ = "Victor Valotto"
__all__ = ['SenialBase', 'SenialLista', 'SenialPila', 'SenialCola', 'FuenteSenial', 'FactorySenial']
