"""
Módulo que define el Factory de contextos de persistencia.
"""
from persistidor_senial.contexto import BaseContexto, ContextoPickle, ContextoArchivo


class FactoryContexto:
    """
    Crea el contexto de persistencia concreto según el tipo y la configuración recibidos.
    """

    @staticmethod
    def crear(tipo, config) -> BaseContexto:
        """
        :param tipo: "pickle" o "archivo"
        :param config: diccionario con los parámetros específicos del tipo
        :return: instancia de ContextoPickle o ContextoArchivo
        """
        recurso = config.get("recurso", "./datos_persistidos")
        if tipo == "pickle":
            return ContextoPickle(recurso)
        elif tipo == "archivo":
            return ContextoArchivo(recurso)
        else:
            raise ValueError(f"Tipo de contexto '{tipo}' no soportado")
