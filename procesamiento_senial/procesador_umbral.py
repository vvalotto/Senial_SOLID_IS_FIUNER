"""
Módulo que define la clase ProcesadorUmbral de señales.
"""
from dominio_senial.senial import Senial


class ProcesadorUmbral:
    """
    Procesador de señales digitales por umbral.

    Clase nueva, agregada sin modificar Procesador. Cualquier valor de
    la señal por encima del umbral configurado se reemplaza por cero.
    """

    def __init__(self, umbral):
        """
        Inicializa el procesador de señales por umbral.

        :param umbral: valor de umbral a partir del cual se filtra
        """
        self._senial_procesada = Senial()
        self._umbral = umbral

    def procesar_senial(self, senial):
        """
        Cada valor de la señal se reemplaza por 0 si supera el umbral.

        :param senial: señal de entrada a procesar
        """
        print("Procesando Señal")
        for i in range(senial.obtener_tamanio()):
            self._senial_procesada.poner_valor(self.funcion_umbral(senial.obtener_valor(i)))

    def obtener_senial_procesada(self):
        """
        Retorna la señal procesada.

        :return: señal con los valores procesados
        """
        return self._senial_procesada

    def funcion_umbral(self, valor):
        """
        Filtra un valor según el umbral configurado.

        :param valor: valor de entrada
        :return: valor original si es menor al umbral, 0 en caso contrario
        """
        return valor if valor < self._umbral else 0
