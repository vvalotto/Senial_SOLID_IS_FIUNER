"""
Paquete procesamiento_senial - Algoritmos de procesamiento

Contiene BaseProcesador, el contrato común que deben cumplir todos los
procesadores, y sus implementaciones concretas: ProcesadorAmplificador
y ProcesadorConUmbral. Depende de dominio_senial.

Versión: 2.1.0
Autor: Victor Valotto
"""

from .procesador import BaseProcesador, ProcesadorAmplificador, ProcesadorConUmbral

__version__ = "2.1.0"
__author__ = "Victor Valotto"
__all__ = ['BaseProcesador', 'ProcesadorAmplificador', 'ProcesadorConUmbral']
