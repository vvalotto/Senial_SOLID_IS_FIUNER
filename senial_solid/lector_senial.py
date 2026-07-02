"""
LectorSenial - clase que concentra lectura, procesamiento y visualización
de una señal digital.
"""


class LectorSenial:
    """
    Clase que posee todas las fases del procesamiento de una señal:
    1. Lectura de la señal
    2. Procesamiento
    3. Visualización de la señal procesada
    """

    def __init__(self, tamanio: int):
        """
        Inicializa la instancia del lector

        :param tamanio: número de valores de la señal a procesar
        """
        self._nro_muestra = tamanio
        self._valores = []
        self._valores_procesados = []

    def __leer_dato_entrada(self) -> float:
        """
        Método privado que se usa para ingresar un solo valor por consola.

        :return: valor numérico ingresado por el usuario
        """
        while True:
            try:
                return float(input('Valor: '))
            except ValueError:
                print('Dato mal ingresado, presione <enter> para continuar')

    def leer_senial(self) -> None:
        """Obtiene la señal de entrada y la guarda en la lista interna"""
        print("Lectura de la señal")
        for i in range(self._nro_muestra):
            print(f"Dato nro: {i + 1}")
            self._valores.append(self.__leer_dato_entrada())

    def procesar_senial(self) -> None:
        """Cada valor adquirido se multiplica por 2"""
        print("Procesando Señal")
        self._valores_procesados = [valor * 2 for valor in self._valores]

    def mostrar_senial(self) -> None:
        """Muestra la señal procesada en salida de consola"""
        print("Señal original:", self._valores)
        print("Señal amplificada (x2):", self._valores_procesados)
