"""
Módulo que define la clase Configurador.
"""
from adquisicion_senial import AdquisidorConsola, AdquisidorArchivo
from procesamiento_senial import BaseProcesador, ProcesadorAmplificador, ProcesadorConUmbral
from presentacion_senial import Visualizador


class Configurador:
    """
    Configurador de la aplicación.

    Centraliza la decisión de qué instancias concretas crear: adquisidor,
    procesador y visualizador.
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

    @staticmethod
    def crear_procesador(tipo_procesamiento, parametro) -> BaseProcesador:
        """
        Crea el procesador concreto según el tipo solicitado.

        :param tipo_procesamiento: "amplificar" o "umbral"
        :param parametro: factor de amplificación o valor de umbral, según el tipo
        :return: instancia de BaseProcesador
        """
        if tipo_procesamiento == "amplificar":
            return ProcesadorAmplificador(parametro)
        elif tipo_procesamiento == "umbral":
            return ProcesadorConUmbral(parametro)
        else:
            raise ValueError(f"Tipo '{tipo_procesamiento}' no soportado")

    @staticmethod
    def crear_visualizador():
        """
        Crea el visualizador de señales configurado para la aplicación.

        :return: instancia de Visualizador
        """
        return Visualizador()
