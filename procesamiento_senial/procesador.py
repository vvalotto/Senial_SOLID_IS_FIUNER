"""
Módulo que define la clase Procesador de señales.
"""
from dominio_senial.senial import Senial


class Procesador:
    """
    Procesador de señales digitales.

    Responsabilidad única: aplicar amplificación x2 a una señal digital.
    No fue modificado para agregar el procesamiento por umbral.
    """

    def __init__(self):
        """
        Inicializa el procesador de señales.
        """
        self._senial_procesada = Senial()

    def procesar_senial(self, senial):
        """
        Cada valor de la señal se multiplica por 2.

        :param senial: señal de entrada a procesar
        """
        print("Procesando Señal")
        self._amplificacion = 2.0
        for i in range(senial.obtener_tamanio()):
            self._senial_procesada.poner_valor(self.funcion_doble(senial.obtener_valor(i)))

    def obtener_senial_procesada(self):
        """
        Retorna la señal procesada.

        :return: señal con los valores procesados
        """
        return self._senial_procesada

    def funcion_doble(self, valor):
        """
        Calcula el doble de un valor, según el factor de amplificación.

        :param valor: valor de entrada
        :return: valor amplificado
        """
        return valor * self._amplificacion
