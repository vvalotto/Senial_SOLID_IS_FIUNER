"""
Paquete adquisicion_senial - Captura de datos de entrada

Contiene BaseAdquisidor, el contrato común que deben cumplir todos los
adquisidores, sus implementaciones concretas (AdquisidorConsola,
AdquisidorArchivo, AdquisidorSenoidal) y FactoryAdquisidor, que las crea
a partir de un tipo y una configuración. Depende de dominio_senial.

Versión: 3.1.0
Autor: Victor Valotto
"""

from .adquisidor import BaseAdquisidor, AdquisidorConsola, AdquisidorArchivo, AdquisidorSenoidal
from .factory_adquisidor import FactoryAdquisidor

__version__ = "3.1.0"
__author__ = "Victor Valotto"
__all__ = ['BaseAdquisidor', 'AdquisidorConsola', 'AdquisidorArchivo', 'AdquisidorSenoidal', 'FactoryAdquisidor']
