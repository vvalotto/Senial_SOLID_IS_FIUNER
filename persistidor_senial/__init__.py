"""
Paquete de persistencia de señales digitales.

Provee estrategias para persistir y recuperar entidades del dominio.
"""
from .persistidor import PersistidorPickle, PersistidorArchivo
from .mapeador import Mapeador, MapeadorArchivo

__version__ = "1.0.0"
__author__ = "Victor Valotto"
__all__ = ['PersistidorPickle', 'PersistidorArchivo', 'Mapeador', 'MapeadorArchivo']
