"""
Módulo que define la clase Configurador.
"""
from adquisicion_senial import AdquisidorConsola, AdquisidorArchivo


class Configurador:
    """
    Configurador de la aplicación.

    Centraliza la decisión de qué adquisidor concreto crear.
    """

    @staticmethod
    def crear_adquisidor():
        """
        Crea el adquisidor configurado por defecto para la aplicación.

        :return: instancia de BaseAdquisidor
        """
        return Configurador.crear_adquisidor_archivo()

    @staticmethod
    def crear_adquisidor_consola():
        """
        Crea un adquisidor que lee la señal desde consola.

        :return: instancia de AdquisidorConsola
        """
        return AdquisidorConsola(5)

    @staticmethod
    def crear_adquisidor_archivo(ruta_archivo='senial.txt'):
        """
        Crea un adquisidor que lee la señal desde un archivo de texto.

        :param ruta_archivo: ruta del archivo a leer
        :return: instancia de AdquisidorArchivo
        """
        return AdquisidorArchivo(ruta_archivo)
