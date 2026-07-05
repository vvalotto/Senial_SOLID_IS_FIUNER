"""
Paquete procesamiento_senial - Algoritmos de procesamiento

Contiene BaseProcesador, el contrato común que deben cumplir todos los
procesadores, sus implementaciones concretas (ProcesadorAmplificador,
ProcesadorConUmbral) y FactoryProcesador, que las crea a partir de un
tipo y una configuración. La señal procesada se recibe inyectada (DIP),
en vez de crearse hardcodeada dentro del procesador. Depende de
dominio_senial.

Versión: 3.0.0
Autor: Victor Valotto
"""

from .procesador import BaseProcesador, ProcesadorAmplificador, ProcesadorConUmbral
from .factory_procesador import FactoryProcesador

__version__ = "3.0.0"
__author__ = "Victor Valotto"
__all__ = ['BaseProcesador', 'ProcesadorAmplificador', 'ProcesadorConUmbral', 'FactoryProcesador']
