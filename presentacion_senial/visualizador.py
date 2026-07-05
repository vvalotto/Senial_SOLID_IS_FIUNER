"""
Módulo que define la clase Visualizador.
"""
from dominio_senial.senial import SenialBase
from dominio_senial.fuente_senial import FuenteSenial


class Visualizador:
    """
    Visualizador de señales y fuentes de señal.

    Responsabilidad única: mostrar los datos de una entidad en consola.
    """

    def mostrar_datos(self, senial: SenialBase, titulo: str) -> None:
        """
        Muestra en consola todos los datos de una señal.

        :param senial: señal a visualizar
        :param titulo: encabezado a mostrar antes de los datos
        """
        valores = [senial.obtener_valor(i) for i in range(senial.obtener_tamanio())]
        print(titulo)
        print(f"  id: {senial.id}")
        print(f"  fecha_adquisicion: {senial.fecha_adquisicion}")
        print(f"  cantidad: {senial.cantidad}")
        print(f"  tamanio: {senial.tamanio}")
        print(f"  valores: {valores}")

    def mostrar_fuente(self, fuente: FuenteSenial, titulo: str) -> None:
        """
        Muestra en consola todos los datos de una fuente de señal.

        :param fuente: fuente de señal a visualizar
        :param titulo: encabezado a mostrar antes de los datos
        """
        print(titulo)
        print(f"  id: {fuente.id}")
        print(f"  nombre: {fuente.nombre}")
        print(f"  descripcion: {fuente.descripcion}")
