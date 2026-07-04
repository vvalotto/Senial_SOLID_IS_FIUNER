"""
Módulo que define la jerarquía de procesadores de señales.
"""
from abc import ABCMeta, abstractmethod
from dominio_senial.senial import Senial


class BaseProcesador(metaclass=ABCMeta):
    """
    Procesador de señales digitales.

    Contrato que cualquier procesador concreto debe cumplir.
    """

    def __init__(self):
        """
        Inicializa el procesador de señales.
        """
        self._senial_procesada = Senial()

    @abstractmethod
    def procesar(self, senial):
        """
        Procesa la señal según el algoritmo de cada implementación concreta.

        :param senial: señal de entrada a procesar
        """
        pass

    def obtener_senial_procesada(self):
        """
        Retorna la señal procesada.

        :return: señal con los valores procesados
        """
        return self._senial_procesada


class ProcesadorAmplificador(BaseProcesador):
    """
    Procesador de señales digitales por amplificación.
    """

    def __init__(self, amplificacion):
        """
        Inicializa el procesador con el factor de amplificación.

        :param amplificacion: factor de amplificación a aplicar
        """
        super().__init__()
        self._amplificacion = amplificacion

    def procesar(self, senial):
        """
        Cada valor de la señal se multiplica por el factor de amplificación.

        :param senial: señal de entrada a procesar
        """
        print("Procesando Señal")
        while senial.cantidad > 0:
            self._senial_procesada.poner_valor(self._amplificar(senial.sacar_valor()))

    def _amplificar(self, valor):
        """
        Calcula el valor amplificado.

        :param valor: valor de entrada
        :return: valor amplificado
        """
        return valor * self._amplificacion


class ProcesadorConUmbral(BaseProcesador):
    """
    Procesador de señales digitales por umbral.
    """

    def __init__(self, umbral):
        """
        Inicializa el procesador con el valor de umbral.

        :param umbral: valor de umbral a partir del cual se filtra
        """
        super().__init__()
        self._umbral = umbral

    def procesar(self, senial):
        """
        Cada valor de la señal se reemplaza por 0 si supera el umbral.

        :param senial: señal de entrada a procesar
        """
        print("Procesando Señal")
        while senial.cantidad > 0:
            self._senial_procesada.poner_valor(self._funcion_umbral(senial.sacar_valor()))

    def _funcion_umbral(self, valor):
        """
        Filtra un valor según el umbral configurado.

        :param valor: valor de entrada
        :return: valor original si es menor al umbral, 0 en caso contrario
        """
        return valor if valor < self._umbral else 0
