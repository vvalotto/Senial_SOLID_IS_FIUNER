"""
Paquete presentacion_senial - Visualización de datos

Contiene la clase Visualizador, responsable de mostrar todos los datos
de una señal (mostrar_datos) o de una fuente de señal (mostrar_fuente).
Depende de dominio_senial y trabaja contra SenialBase/FuenteSenial, no
contra implementaciones concretas.

Versión: 2.1.0
Autor: Victor Valotto
"""

from .visualizador import Visualizador

__version__ = "2.1.0"
__author__ = "Victor Valotto"
__all__ = ['Visualizador']
