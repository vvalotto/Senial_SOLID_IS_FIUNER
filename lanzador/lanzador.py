#!/usr/bin/env python3
"""
Lanzador - punto de entrada del sistema de procesamiento de señales
"""

import hashlib
import uuid
from datetime import date

from dominio_senial import FuenteSenial
from configurador import Configurador


class Lanzador:
    """
    Orquesta la ejecución del pipeline: fuente, adquisición, procesamiento y visualización.

    No conoce ningún tipo concreto — todas las dependencias las determina
    config.json a través de Configurador.
    """

    @staticmethod
    def _generar_id() -> str:
        """Genera un identificador único (hash) para una entidad a persistir."""
        return hashlib.sha256(uuid.uuid4().bytes).hexdigest()[:12]

    @staticmethod
    def ejecutar() -> None:
        """Ejecuta el pipeline completo: registrar fuente, adquirir, guardar, procesar, guardar, obtener y mostrar"""
        Configurador.inicializar_configuracion()
        visualizador = Configurador.crear_visualizador()

        # Registro de la fuente de la señal, previo a tratar la señal en sí
        repositorio_fuente = Configurador.crear_repositorio_fuente_senial()
        nombre_fuente = input("Nombre de la fuente de señal: ")
        descripcion_fuente = input("Descripción de la fuente de señal: ")
        fuente_senial = FuenteSenial(nombre_fuente, descripcion_fuente)
        fuente_senial.id = Lanzador._generar_id()
        repositorio_fuente.guardar(fuente_senial)

        adquisidor = Configurador.crear_adquisidor()
        repositorio_adquisicion = Configurador.crear_repositorio_adquisicion()

        adquisidor.leer_senial()
        senial_adquirida = adquisidor.obtener_senial_adquirida()
        senial_adquirida.id = Lanzador._generar_id()
        senial_adquirida.fecha_adquisicion = date.today()
        repositorio_adquisicion.guardar(senial_adquirida)
        repositorio_adquisicion.auditar(senial_adquirida, f"Señal adquirida con {senial_adquirida.cantidad} valores")
        repositorio_adquisicion.trazar(senial_adquirida, "ADQUISICION", "Lectura completada")

        procesador = Configurador.crear_procesador()
        procesador.procesar(senial_adquirida)
        senial_procesada = procesador.obtener_senial_procesada()
        senial_procesada.id = Lanzador._generar_id()
        senial_procesada.fecha_adquisicion = senial_adquirida.fecha_adquisicion
        repositorio_procesamiento = Configurador.crear_repositorio_procesamiento()
        repositorio_procesamiento.guardar(senial_procesada)
        repositorio_procesamiento.auditar(senial_procesada, f"Señal procesada con {type(procesador).__name__}")
        repositorio_procesamiento.trazar(senial_procesada, "PROCESAMIENTO", "Procesamiento completado")

        senial_adquirida_recuperada = repositorio_adquisicion.obtener(senial_adquirida.id)
        senial_procesada_recuperada = repositorio_procesamiento.obtener(senial_procesada.id)
        fuente_recuperada = repositorio_fuente.obtener(fuente_senial.id)

        visualizador.mostrar_fuente(fuente_recuperada, "Fuente de señal (recuperada):")
        visualizador.mostrar_datos(senial_adquirida_recuperada, "Señal original (recuperada):")
        visualizador.mostrar_datos(senial_procesada_recuperada, "Señal procesada (recuperada):")


def ejecutar() -> None:
    """Punto de entrada para el comando de consola (ver setup.py)"""
    Lanzador.ejecutar()


if __name__ == "__main__":
    ejecutar()
