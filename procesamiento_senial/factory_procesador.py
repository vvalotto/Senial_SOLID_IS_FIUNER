"""
Módulo que define el Factory de procesadores.
"""
from procesamiento_senial.procesador import BaseProcesador, ProcesadorAmplificador, ProcesadorConUmbral


class FactoryProcesador:
    """
    Crea el procesador concreto según el tipo y la configuración recibidos.
    """

    @staticmethod
    def crear(tipo, config) -> BaseProcesador:
        """
        :param tipo: "amplificador" o "umbral"
        :param config: diccionario con los parámetros específicos del tipo
        :return: instancia de BaseProcesador
        """
        if tipo == "amplificador":
            return ProcesadorAmplificador(config.get("factor", 4.0))
        elif tipo == "umbral":
            return ProcesadorConUmbral(config.get("umbral", 100))
        else:
            raise ValueError(f"Tipo de procesador '{tipo}' no soportado")
