"""
Módulo que define la clase Procesador de señales.
"""
from dominio_senial.senial import Senial


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

    def procesar_amplificar(self, senial, parametro):
        """
        Procesa la señal amplificando cada valor.

        :param senial: señal de entrada a procesar
        :param parametro: factor de amplificación
        """
        print("Procesando Señal")
        self._amplificacion = parametro
        for i in range(senial.obtener_tamanio()):
            self._senial_procesada.poner_valor(self.funcion_doble(senial.obtener_valor(i)))

    def procesar_umbral(self, senial, parametro):
        """
        Procesa la señal aplicando un umbral.

        :param senial: señal de entrada a procesar
        :param parametro: valor de umbral
        """
        print("Procesando Señal")
        self._umbral = parametro
        for i in range(senial.obtener_tamanio()):
            self._senial_procesada.poner_valor(self.funcion_umbral(senial.obtener_valor(i)))

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

    def funcion_umbral(self, valor):
        """
        Filtra un valor según el umbral configurado.

        :param valor: valor de entrada
        :return: valor original si es menor al umbral, 0 en caso contrario
        """
        return valor if valor < self._umbral else 0
