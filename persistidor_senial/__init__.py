"""
Paquete de persistencia de señales digitales.

Provee estrategias para persistir y recuperar entidades del dominio.
"""
from .persistidor import BasePersistidor, PersistidorPickle, PersistidorArchivo
from .mapeador import Mapeador, MapeadorArchivo

__version__ = "1.1.1"
__author__ = "Victor Valotto"
__all__ = ['BasePersistidor', 'PersistidorPickle', 'PersistidorArchivo', 'Mapeador', 'MapeadorArchivo']
