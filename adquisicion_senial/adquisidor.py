"""
Módulo que define la jerarquía de adquisidores de señales.
"""
from abc import ABCMeta, abstractmethod


class BaseAdquisidor(metaclass=ABCMeta):
    """
    Adquisidor de señales digitales.

    Contrato que cualquier adquisidor concreto debe cumplir.
    """

    def __init__(self, numero_muestras, senial):
        """
        Inicializa el adquisidor de señales.

        :param numero_muestras: cantidad de muestras a adquirir
        :param senial: instancia de señal donde se almacenan los datos adquiridos
        """
        self._senial = senial
        self._numero_muestras = numero_muestras

    def obtener_senial_adquirida(self):
        """
        Retorna la señal con los valores adquiridos.

        :return: señal con los datos capturados
        """
        return self._senial

    @abstractmethod
    def leer_senial(self):
        """
        Obtiene los datos de entrada y los almacena en la señal.
        """
        pass


class AdquisidorConsola(BaseAdquisidor):
    """
    Adquisidor de señales digitales desde consola.
    """

    @staticmethod
    def _leer_dato_entrada():
        """
        Método privado que se usa para ingresar un solo valor por consola.

        :return: valor numérico ingresado por el usuario
        """
        while True:
            try:
                return float(input('Ingresar Valor: '))
            except ValueError:
                print('Dato mal ingresado. Ingresá un número válido.')

    def leer_senial(self):
        """Obtiene la señal de entrada desde consola y la guarda en la señal"""
        print("Lectura de la señal desde consola")
        for i in range(self._numero_muestras):
            print(f"Dato nro: {i}")
            self._senial.poner_valor(self._leer_dato_entrada())


class AdquisidorArchivo(BaseAdquisidor):
    """
    Adquisidor de señales digitales desde archivo de texto.
    """

    def __init__(self, ruta_archivo, senial):
        """
        Inicializa el adquisidor de señales por archivo.

        :param ruta_archivo: ruta del archivo de texto a leer
        :param senial: instancia de señal donde se almacenan los datos adquiridos
        """
        super().__init__(0, senial)
        self._ruta_archivo = ruta_archivo

    def leer_senial(self):
        """Obtiene la señal de entrada desde un archivo y la guarda en la señal"""
        print(f"Lectura de la señal desde archivo: {self._ruta_archivo}")
        with open(self._ruta_archivo, 'r', encoding='utf-8') as archivo:
            for linea in archivo:
                try:
                    self._senial.poner_valor(float(linea.strip()))
                except ValueError:
                    continue
