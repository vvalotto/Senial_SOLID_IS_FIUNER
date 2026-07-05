"""
Paquete configurador - Factory centralizado

Contiene Configurador, que lee config.json (vía CargadorConfig) y delega
la creación de cada instancia concreta a su Factory especializado
(FactorySenial, FactoryAdquisidor, FactoryProcesador, FactoryContexto).
Sin if/elif propios — DIP completo: la configuración externa determina
todas las dependencias del sistema.

Versión: 3.0.0
Autor: Victor Valotto
"""

from .configurador import Configurador
from .cargador_config import CargadorConfig

__version__ = "3.0.0"
__author__ = "Victor Valotto"
__all__ = ['Configurador', 'CargadorConfig']
