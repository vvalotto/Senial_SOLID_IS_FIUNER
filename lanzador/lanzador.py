#!/usr/bin/env python3
"""
Lanzador - punto de entrada del sistema de procesamiento de señales
"""

from adquisicion_senial import Adquisidor
from procesamiento_senial import BaseProcesador, ProcesadorAmplificador, ProcesadorConUmbral
from presentacion_senial import Visualizador


class Lanzador:
    """Orquesta la ejecución del pipeline: leer, procesar y mostrar la señal."""

    @staticmethod
    def crear_procesador(tipo_procesamiento, parametro) -> BaseProcesador:
        """
        Factory: crea el procesador concreto según el tipo solicitado.

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
    def ejecutar() -> None:
        """Ejecuta el pipeline completo sobre una señal de 10 muestras"""
        adquisidor = Adquisidor(10)
        visualizador = Visualizador()

        adquisidor.leer_senial()
        senial_adquirida = adquisidor.obtener_senial_adquirida()

        tipo_procesamiento = "umbral"
        parametro = 5.0

        procesador = Lanzador.crear_procesador(tipo_procesamiento, parametro)
        procesador.procesar(senial_adquirida)
        senial_procesada = procesador.obtener_senial_procesada()

        visualizador.mostrar_datos(senial_adquirida, "Señal original:")
        visualizador.mostrar_datos(senial_procesada, "Señal con umbral aplicado (umbral=5.0):")


def ejecutar() -> None:
    """Punto de entrada para el comando de consola (ver setup.py)"""
    Lanzador.ejecutar()


if __name__ == "__main__":
    ejecutar()
