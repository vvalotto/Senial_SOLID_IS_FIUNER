"""
Paquete supervisor - Contratos de supervisión del sistema.

No persiste datos ni procesa señales. Su única responsabilidad es
definir qué significa auditar y qué significa trazar, separado de
la persistencia (persistidor_senial).
"""
from .auditor import BaseAuditor
from .trazador import BaseTrazador

__version__ = "1.0.0"
__author__ = "Victor Valotto"
__all__ = ['BaseAuditor', 'BaseTrazador']
