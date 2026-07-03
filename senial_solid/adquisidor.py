"""
Módulo que define la clase Adquisidor de señales.
"""
from senial_solid.senial import Senial


class Adquisidor:
    """
    Adquisidor de datos para señales digitales.

    Responsabilidad única: capturar datos de entrada desde consola
    y construir una señal digital.
    """

    def __init__(self, nro_muestras):
        """
        Inicializa el adquisidor de señales.

        :param nro_muestras: cantidad de muestras a adquirir
        """
        self._senial = Senial()
        self._nro_muestra = nro_muestras

    def __leer_dato_entrada(self):
        """
        Método privado que se usa para ingresar un solo valor por consola.

        :return: valor numérico ingresado por el usuario
        """
        while True:
            try:
                return float(input('Valor: '))
            except ValueError:
                print('Dato mal ingresado, presione <enter> para continuar')

    def leer_senial(self):
        """Obtiene la señal de entrada y la guarda en la entidad Senial"""
        print("Lectura de la señal")
        for i in range(self._nro_muestra):
            print(f"Dato nro: {i + 1}")
            self._senial.poner_valor(self.__leer_dato_entrada())

    def obtener_senial_adquirida(self):
        """
        Retorna la señal con los valores adquiridos.

        :return: señal con los datos capturados
        """
        return self._senial
