"""
Módulo que define la entidad Senial.
Representa una señal digital como entidad del dominio.
"""


class Senial:
    """
    Entidad que representa una señal digital.

    Almacena los valores de la señal y expone operaciones básicas
    de acceso y modificación.
    """

    def __init__(self):
        """
        Inicializa una nueva señal digital vacía.
        """
        self._valores = []

    def poner_valor(self, valor):
        """
        Agrega un nuevo valor al final de la señal.

        :param valor: valor numérico a agregar a la señal
        """
        self._valores.append(valor)

    def obtener_valor(self, indice):
        """
        Recupera un valor de la señal por su índice.

        :param indice: índice del valor a recuperar (base 0)
        :return: valor en la posición especificada
        """
        return self._valores[indice]

    def obtener_tamanio(self):
        """
        Retorna el número de muestras en la señal.

        :return: cantidad de valores almacenados en la señal
        """
        return len(self._valores)
