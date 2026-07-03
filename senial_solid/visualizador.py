"""
Módulo que define la clase Visualizador de señales.
"""
from senial_solid.senial import Senial


class Visualizador:
    """
    Visualizador de señales digitales.

    Responsabilidad única: mostrar los datos de una señal digital en consola.
    """

    def mostrar_datos(self, senial: Senial, titulo: str) -> None:
        """
        Muestra en consola los valores de una señal.

        :param senial: señal a visualizar
        :param titulo: encabezado a mostrar antes de los valores
        """
        valores = [senial.obtener_valor(i) for i in range(senial.obtener_tamanio())]
        print(titulo, valores)
