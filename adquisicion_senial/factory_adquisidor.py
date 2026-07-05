"""
Módulo que define el Factory de adquisidores.
"""
from adquisicion_senial.adquisidor import BaseAdquisidor, AdquisidorConsola, AdquisidorArchivo, AdquisidorSenoidal


class FactoryAdquisidor:
    """
    Crea el adquisidor concreto según el tipo y la configuración recibidos.
    """

    @staticmethod
    def crear(tipo, config, senial) -> BaseAdquisidor:
        """
        :param tipo: "consola", "archivo" o "senoidal"
        :param config: diccionario con los parámetros específicos del tipo
        :param senial: instancia de señal donde se almacenan los datos adquiridos
        :return: instancia de BaseAdquisidor
        """
        if tipo == "consola":
            return AdquisidorConsola(config.get("num_muestras", 5), senial)
        elif tipo == "archivo":
            return AdquisidorArchivo(config.get("ruta_archivo", "senial.txt"), senial)
        elif tipo == "senoidal":
            return AdquisidorSenoidal(config.get("num_muestras", 10), senial)
        else:
            raise ValueError(f"Tipo de adquisidor '{tipo}' no soportado")
