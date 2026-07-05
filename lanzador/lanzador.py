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
        return Configurador.crear_adquisidor(origen, tipo_senial)

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
    def seleccionar_repositorio_senial():
        """
        Solicita al usuario la estrategia de persistencia y crea el repositorio de señales.

        :return: instancia de RepositorioSenial
        """
        tipo_contexto = input("Persistencia de señales (pickle/archivo): ").strip().lower()
        contexto = Configurador.crear_contexto(tipo_contexto, "datos_persistidos")
        return Configurador.crear_repositorio("senial", contexto)

    @staticmethod
    def ejecutar() -> None:
        """Ejecuta el pipeline completo: adquirir, guardar, procesar, guardar, obtener y mostrar"""
        adquisidor = Lanzador.seleccionar_adquisidor()
        visualizador = Configurador.crear_visualizador()
        repositorio_senial = Lanzador.seleccionar_repositorio_senial()

        adquisidor.leer_senial()
        senial_adquirida = adquisidor.obtener_senial_adquirida()
        senial_adquirida.id = 1
        repositorio_senial.guardar(senial_adquirida)

        procesador = Lanzador.seleccionar_procesador()
        procesador.procesar(senial_adquirida)
        senial_procesada = procesador.obtener_senial_procesada()
        senial_procesada.id = 2
        repositorio_senial.guardar(senial_procesada)

        senial_adquirida_recuperada = repositorio_senial.obtener("1")
        senial_procesada_recuperada = repositorio_senial.obtener("2")

        visualizador.mostrar_datos(senial_adquirida_recuperada, "Señal original (recuperada):")
        visualizador.mostrar_datos(senial_procesada_recuperada, "Señal procesada (recuperada):")


def ejecutar() -> None:
    """Punto de entrada para el comando de consola (ver setup.py)"""
    Lanzador.ejecutar()


if __name__ == "__main__":
    ejecutar()
