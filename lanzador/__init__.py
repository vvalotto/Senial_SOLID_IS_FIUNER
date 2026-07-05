"""
Paquete lanzador - Orquestador principal del sistema

Contiene Lanzador, que solo orquesta el flujo: obtener componentes
desde Configurador, ejecutar el pipeline (adquirir, persistir,
procesar, persistir, recuperar y mostrar) y presentar resultados.
Toda la creación de instancias (adquisidor, procesador, visualizador,
persistidor) se delega en el paquete configurador.

Versión: 2.2.0
Autor: Victor Valotto
"""

from .lanzador import Lanzador, ejecutar

__version__ = "2.2.0"
__author__ = "Victor Valotto"
__all__ = ['Lanzador', 'ejecutar']
