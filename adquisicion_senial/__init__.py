"""
Paquete adquisicion_senial - Captura de datos de entrada

Contiene BaseAdquisidor, el contrato común que deben cumplir todos los
adquisidores, y sus implementaciones concretas: AdquisidorConsola y
AdquisidorArchivo. Depende de dominio_senial.

Versión: 3.0.1
Autor: Victor Valotto
"""

from .adquisidor import BaseAdquisidor, AdquisidorConsola, AdquisidorArchivo

__version__ = "3.0.1"
__author__ = "Victor Valotto"
__all__ = ['BaseAdquisidor', 'AdquisidorConsola', 'AdquisidorArchivo']
