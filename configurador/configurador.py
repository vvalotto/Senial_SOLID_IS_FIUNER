"""
Módulo que define la clase Configurador.
"""
from adquisicion_senial import AdquisidorConsola, AdquisidorArchivo
from dominio_senial import Senial, SenialPila, SenialCola
from procesamiento_senial import BaseProcesador, ProcesadorAmplificador, ProcesadorConUmbral
from presentacion_senial import Visualizador


class Configurador:
    """
    Configurador de la aplicación.

    Centraliza la decisión de qué instancias concretas crear: señal,
    adquisidor, procesador y visualizador.
    """

    @staticmethod
    def crear_senial(tipo_senial='lista', tamanio=10):
        """
        Crea la señal concreta según el tipo solicitado.

        :param tipo_senial: "lista", "pila" o "cola"
        :param tamanio: tamaño de la señal
        :return: instancia de Senial, SenialPila o SenialCola
        """
        if tipo_senial == "pila":
            return SenialPila(tamanio)
        elif tipo_senial == "cola":
            return SenialCola(tamanio)
        else:
            return Senial(tamanio)

    @staticmethod
    def crear_adquisidor():
        """
        Crea el adquisidor configurado por defecto para la aplicación.

        :return: instancia de BaseAdquisidor
        """
        return Configurador.crear_adquisidor_archivo()

    @staticmethod
    def crear_adquisidor_consola(tipo_senial='lista'):
        """
        Crea un adquisidor que lee la señal desde consola.

        :param tipo_senial: "lista", "pila" o "cola"
        :return: instancia de AdquisidorConsola
        """
        return AdquisidorConsola(5, Configurador.crear_senial(tipo_senial, 5))

    @staticmethod
    def crear_adquisidor_archivo(ruta_archivo='senial.txt', tipo_senial='lista'):
        """
        Crea un adquisidor que lee la señal desde un archivo de texto.

        :param ruta_archivo: ruta del archivo a leer
        :param tipo_senial: "lista", "pila" o "cola"
        :return: instancia de AdquisidorArchivo
        """
        return AdquisidorArchivo(ruta_archivo, Configurador.crear_senial(tipo_senial, 10))

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
