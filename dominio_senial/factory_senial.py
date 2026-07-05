"""
Módulo que define el Factory de señales.
"""
from dominio_senial.senial import SenialBase, SenialLista, SenialPila, SenialCola


class FactorySenial:
    """
    Crea la señal concreta según el tipo y la configuración recibidos.
    """

    @staticmethod
    def crear(tipo, config) -> SenialBase:
        """
        :param tipo: "lista", "pila" o "cola"
        :param config: diccionario con los parámetros específicos del tipo
        :return: instancia de SenialLista, SenialPila o SenialCola
        """
        tamanio = config.get("tamanio", 10)
        if tipo == "lista":
            return SenialLista(tamanio)
        elif tipo == "pila":
            return SenialPila(tamanio)
        elif tipo == "cola":
            return SenialCola(tamanio)
        else:
            raise ValueError(f"Tipo de señal '{tipo}' no soportado")
