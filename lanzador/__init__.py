"""
Paquete lanzador - Orquestador principal del sistema

Contiene Lanzador, que solo orquesta el flujo: obtener componentes
desde Configurador, ejecutar el pipeline y mostrar resultados. Toda
la creación de instancias (adquisidor, procesador, visualizador) se
delega en el paquete configurador.

Versión: 2.0.0
Autor: Victor Valotto
"""

from .lanzador import Lanzador, ejecutar

__version__ = "2.0.0"
__author__ = "Victor Valotto"
__all__ = ['Lanzador', 'ejecutar']
