"""
Módulo que define el Factory de procesadores.
"""
from procesamiento_senial.procesador import BaseProcesador, ProcesadorAmplificador, ProcesadorConUmbral


class FactoryProcesador:
    """
    Crea el procesador concreto según el tipo y la configuración recibidos.
    """

    @staticmethod
    def crear(tipo, config, senial) -> BaseProcesador:
        """
        :param tipo: "amplificador" o "umbral"
        :param config: diccionario con los parámetros específicos del tipo
        :param senial: instancia de señal donde se almacenan los valores procesados
        :return: instancia de BaseProcesador
        """
        if tipo == "amplificador":
            return ProcesadorAmplificador(config.get("factor", 4.0), senial)
        elif tipo == "umbral":
            return ProcesadorConUmbral(config.get("umbral", 100), senial)
        else:
            raise ValueError(f"Tipo de procesador '{tipo}' no soportado")
