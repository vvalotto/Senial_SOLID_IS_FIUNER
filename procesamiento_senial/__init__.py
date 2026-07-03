"""
Paquete procesamiento_senial - Algoritmos de procesamiento

Contiene Procesador (amplificación) y ProcesadorUmbral (filtrado por
umbral), sin contrato común entre sí. Depende de dominio_senial.

Versión: 1.3.0
Autor: Victor Valotto
"""

from .procesador import Procesador
from .procesador_umbral import ProcesadorUmbral

__version__ = "1.3.0"
__author__ = "Victor Valotto"
__all__ = ['Procesador', 'ProcesadorUmbral']
