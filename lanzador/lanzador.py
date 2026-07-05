#!/usr/bin/env python3
"""
Lanzador - punto de entrada del sistema de procesamiento de señales
"""

from dominio_senial import FuenteSenial
from configurador import Configurador


class Lanzador:
    """Orquesta la ejecución del pipeline: fuente, adquisición, procesamiento y visualización."""

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
    def seleccionar_repositorio(tipo_entidad, tipo_contexto):
        """
        Crea el repositorio de la entidad solicitada, con el tipo de contexto indicado.

        :param tipo_entidad: "senial" o "fuente_senial"
        :param tipo_contexto: "pickle" o "archivo"
        :return: instancia de BaseRepositorio
        """
        contexto = Configurador.crear_contexto(tipo_contexto, f"datos_persistidos/{tipo_entidad}")
        return Configurador.crear_repositorio(tipo_entidad, contexto)

    @staticmethod
    def ejecutar() -> None:
        """Ejecuta el pipeline completo: registrar fuente, adquirir, guardar, procesar, guardar, obtener y mostrar"""
        tipo_contexto = input("Persistencia (pickle/archivo): ").strip().lower()
        visualizador = Configurador.crear_visualizador()

        # Registro de la fuente de la señal, previo a tratar la señal en sí
        repositorio_fuente = Lanzador.seleccionar_repositorio("fuente_senial", tipo_contexto)
        nombre_fuente = input("Nombre de la fuente de señal: ")
        descripcion_fuente = input("Descripción de la fuente de señal: ")
        fuente_senial = FuenteSenial(nombre_fuente, descripcion_fuente)
        fuente_senial.id = 1
        repositorio_fuente.guardar(fuente_senial)

        adquisidor = Lanzador.seleccionar_adquisidor()
        repositorio_senial = Lanzador.seleccionar_repositorio("senial", tipo_contexto)

        adquisidor.leer_senial()
        senial_adquirida = adquisidor.obtener_senial_adquirida()
        senial_adquirida.id = 1
        repositorio_senial.guardar(senial_adquirida)
        repositorio_senial.auditar(senial_adquirida, f"Señal adquirida con {senial_adquirida.cantidad} valores")
        repositorio_senial.trazar(senial_adquirida, "ADQUISICION", "Lectura completada")

        procesador = Lanzador.seleccionar_procesador()
        procesador.procesar(senial_adquirida)
        senial_procesada = procesador.obtener_senial_procesada()
        senial_procesada.id = 2
        repositorio_senial.guardar(senial_procesada)
        repositorio_senial.auditar(senial_procesada, f"Señal procesada con {type(procesador).__name__}")
        repositorio_senial.trazar(senial_procesada, "PROCESAMIENTO", "Procesamiento completado")

        senial_adquirida_recuperada = repositorio_senial.obtener("1")
        senial_procesada_recuperada = repositorio_senial.obtener("2")
        fuente_recuperada = repositorio_fuente.obtener("1")

        print(f"Fuente de señal (recuperada): {fuente_recuperada.nombre} - {fuente_recuperada.descripcion}")
        visualizador.mostrar_datos(senial_adquirida_recuperada, "Señal original (recuperada):")
        visualizador.mostrar_datos(senial_procesada_recuperada, "Señal procesada (recuperada):")


def ejecutar() -> None:
    """Punto de entrada para el comando de consola (ver setup.py)"""
    Lanzador.ejecutar()


if __name__ == "__main__":
    ejecutar()
