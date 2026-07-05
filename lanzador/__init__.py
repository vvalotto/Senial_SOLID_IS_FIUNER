"""
Paquete lanzador - Orquestador principal del sistema

Contiene Lanzador, orquestador puro (DIP): no conoce ningún tipo
concreto ni pregunta configuración por consola — todas las dependencias
las determina config.json a través de Configurador. Solo pide datos de
dominio (nombre/descripción de la fuente de señal).

Versión: 3.0.0
Autor: Victor Valotto
"""

from .lanzador import Lanzador, ejecutar

__version__ = "3.0.0"
__author__ = "Victor Valotto"
__all__ = ['Lanzador', 'ejecutar']
