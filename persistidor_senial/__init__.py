"""
Paquete de persistencia de señales digitales.

Provee estrategias de persistencia (Contexto) y el patrón Repository,
que separa la lógica de dominio de esas estrategias mediante DIP.
RepositorioSenial declara explícitamente sus capacidades de auditoría
y trazabilidad heredando de supervisor.BaseAuditor/BaseTrazador (ISP).
"""
from .contexto import BaseContexto, ContextoPickle, ContextoArchivo
from .repositorio import BaseRepositorio, RepositorioSenial, RepositorioFuenteSenial
from .mapeador import Mapeador, MapeadorArchivo
from .factory_contexto import FactoryContexto

__version__ = "4.2.0"
__author__ = "Victor Valotto"
__all__ = [
    'BaseContexto', 'ContextoPickle', 'ContextoArchivo',
    'BaseRepositorio', 'RepositorioSenial', 'RepositorioFuenteSenial',
    'Mapeador', 'MapeadorArchivo', 'FactoryContexto',
]
