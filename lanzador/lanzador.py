#!/usr/bin/env python3
"""
Lanzador - punto de entrada del sistema de procesamiento de señales
"""

from configurador import Configurador


class Lanzador:
    """Orquesta la ejecución del pipeline: leer, procesar y mostrar la señal."""

    @staticmethod
    def seleccionar_adquisidor():
        """
        Solicita al usuario el origen de la señal y crea el adquisidor correspondiente.

        :return: instancia de BaseAdquisidor
        """
        origen = input("Origen de la señal (consola/archivo): ").strip().lower()
        tipo_senial = input("Tipo de señal (lista/pila/cola): ").strip().lower()
        if origen == "consola":
            return Configurador.crear_adquisidor_consola(tipo_senial)
        return Configurador.crear_adquisidor_archivo(tipo_senial=tipo_senial)

    @staticmethod
    def seleccionar_procesador():
        """
        Solicita al usuario el tipo de procesamiento y crea el procesador correspondiente.

        :return: instancia de BaseProcesador
        """
        tipo_procesamiento = input("Tipo de procesamiento (amplificar/umbral): ").strip().lower()
        parametro = float(input("Parámetro (factor de amplificación o umbral): "))
        return Configurador.crear_procesador(tipo_procesamiento, parametro)

    @staticmethod
    def ejecutar() -> None:
        """Ejecuta el pipeline completo sobre la señal adquirida"""
        adquisidor = Lanzador.seleccionar_adquisidor()
        visualizador = Configurador.crear_visualizador()

        adquisidor.leer_senial()
        senial_adquirida = adquisidor.obtener_senial_adquirida()

        procesador = Lanzador.seleccionar_procesador()
        procesador.procesar(senial_adquirida)
        senial_procesada = procesador.obtener_senial_procesada()

        visualizador.mostrar_datos(senial_adquirida, "Señal original:")
        visualizador.mostrar_datos(senial_procesada, "Señal procesada:")


def ejecutar() -> None:
    """Punto de entrada para el comando de consola (ver setup.py)"""
    Lanzador.ejecutar()


if __name__ == "__main__":
    ejecutar()
