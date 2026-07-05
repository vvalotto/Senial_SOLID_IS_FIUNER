"""
Paquete lanzador - Orquestador principal del sistema

Contiene Lanzador, que solo orquesta el flujo: registrar la fuente de
la señal, adquirir, guardar, auditar, trazar, procesar, guardar,
auditar, trazar, obtener y mostrar. Toda la creación de instancias
(adquisidor, procesador, visualizador, contexto, repositorio) se
delega en el paquete configurador.

Versión: 2.5.0
Autor: Victor Valotto
"""

from .lanzador import Lanzador, ejecutar

__version__ = "2.5.0"
__author__ = "Victor Valotto"
__all__ = ['Lanzador', 'ejecutar']
