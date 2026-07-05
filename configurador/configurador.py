"""
Módulo que define la clase Configurador.
"""
from adquisicion_senial import BaseAdquisidor, AdquisidorConsola, AdquisidorArchivo
from dominio_senial import SenialLista, SenialPila, SenialCola
from procesamiento_senial import BaseProcesador, ProcesadorAmplificador, ProcesadorConUmbral
from presentacion_senial import Visualizador
from persistidor_senial import (
    ContextoPickle, ContextoArchivo, BaseRepositorio, RepositorioSenial, RepositorioFuenteSenial,
)


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
        :return: instancia de SenialLista, SenialPila o SenialCola
        """
        if tipo_senial == "lista":
            return SenialLista(tamanio)
        elif tipo_senial == "pila":
            return SenialPila(tamanio)
        elif tipo_senial == "cola":
            return SenialCola(tamanio)
        else:
            raise ValueError(f"Tipo de señal '{tipo_senial}' no soportado")

    @staticmethod
    def crear_adquisidor(origen, tipo_senial='lista') -> BaseAdquisidor:
        """
        Crea el adquisidor concreto según el origen solicitado.

        :param origen: "consola" o "archivo"
        :param tipo_senial: "lista", "pila" o "cola"
        :return: instancia de BaseAdquisidor
        """
        if origen == "consola":
            return AdquisidorConsola(5, Configurador.crear_senial(tipo_senial, 5))
        elif origen == "archivo":
            return AdquisidorArchivo('senial.txt', Configurador.crear_senial(tipo_senial, 10))
        else:
            raise ValueError(f"Origen '{origen}' no soportado")

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
    def crear_contexto(tipo_contexto, recurso):
        """
        Crea el contexto de persistencia concreto según el tipo solicitado.

        :param tipo_contexto: "pickle" o "archivo"
        :param recurso: directorio donde persistir/recuperar las entidades
        :return: instancia de ContextoPickle o ContextoArchivo
        """
        if tipo_contexto == "pickle":
            return ContextoPickle(recurso)
        elif tipo_contexto == "archivo":
            return ContextoArchivo(recurso)
        else:
            raise ValueError(f"Tipo de contexto '{tipo_contexto}' no soportado")

    @staticmethod
    def crear_repositorio(tipo_entidad, contexto) -> BaseRepositorio:
        """
        Crea el repositorio concreto según el tipo de entidad solicitado.

        :param tipo_entidad: "senial" o "fuente_senial"
        :param contexto: instancia de BaseContexto inyectada en el repositorio
        :return: instancia de RepositorioSenial o RepositorioFuenteSenial
        """
        if tipo_entidad == "senial":
            return RepositorioSenial(contexto)
        elif tipo_entidad == "fuente_senial":
            return RepositorioFuenteSenial(contexto)
        else:
            raise ValueError(f"Tipo de entidad '{tipo_entidad}' no soportado")

    @staticmethod
    def crear_visualizador():
        """
        Crea el visualizador de señales configurado para la aplicación.

        :return: instancia de Visualizador
        """
        return Visualizador()
