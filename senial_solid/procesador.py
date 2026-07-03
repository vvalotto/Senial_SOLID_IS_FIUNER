"""
Módulo que define la clase Procesador de señales.
"""
from senial_solid.senial import Senial


class Procesador:
    """
    Procesador de señales digitales.

    Responsabilidad única: aplicar amplificación x2 a una señal digital.
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
        for i in range(senial.obtener_tamanio()):
            self._senial_procesada.poner_valor(senial.obtener_valor(i) * 2)

    def obtener_senial_procesada(self):
        """
        Retorna la señal procesada.

        :return: señal con los valores procesados
        """
        return self._senial_procesada
