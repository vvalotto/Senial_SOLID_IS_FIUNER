"""
Módulo que define la jerarquía de señales digitales.
Representa una señal digital como entidad del dominio.
"""
from abc import ABC, abstractmethod
from typing import Any, List, Optional


class SenialBase(ABC):
    """
    Contrato común que debe cumplir cualquier señal digital.
    """

    def __init__(self, tamanio: int = 10):
        """
        Inicializa los atributos comunes a cualquier señal.

        :param tamanio: tamaño máximo de la señal
        """
        self._fecha_adquisicion = None
        self._cantidad = 0
        self._tamanio = tamanio

    @property
    def fecha_adquisicion(self) -> Any:
        return self._fecha_adquisicion

    @fecha_adquisicion.setter
    def fecha_adquisicion(self, valor) -> None:
        self._fecha_adquisicion = valor

    @property
    def cantidad(self) -> int:
        return self._cantidad

    @cantidad.setter
    def cantidad(self, valor) -> None:
        self._cantidad = valor

    @property
    def tamanio(self) -> int:
        return self._tamanio

    @tamanio.setter
    def tamanio(self, valor) -> None:
        self._tamanio = valor

    @abstractmethod
    def poner_valor(self, valor: float) -> None:
        """Agrega un valor a la señal, según la semántica de cada implementación."""
        pass

    @abstractmethod
    def sacar_valor(self) -> Optional[float]:
        """Extrae un valor de la señal, según la semántica de cada implementación."""
        pass

    @abstractmethod
    def obtener_valor(self, indice: int) -> Optional[float]:
        """Recupera un valor de la señal por índice."""
        pass

    @abstractmethod
    def obtener_tamanio(self) -> int:
        """Retorna la cantidad real de valores almacenados en la señal."""
        pass

    @abstractmethod
    def limpiar(self) -> None:
        """Vacía la señal por completo."""
        pass


class SenialLista(SenialBase):
    """
    Señal digital con comportamiento de lista dinámica.
    """

    def __init__(self, tamanio: int = 10):
        """
        Inicializa una nueva señal digital vacía.

        :param tamanio: tamaño máximo de la señal
        """
        super().__init__(tamanio)
        self._valores: List[float] = []

    @property
    def valores(self) -> List[float]:
        return self._valores

    @valores.setter
    def valores(self, datos: List[float]) -> None:
        self._valores = datos

    def poner_valor(self, valor):
        """
        Agrega un nuevo valor a la señal.

        :param valor: valor numérico a agregar a la señal
        """
        if self._cantidad >= self._tamanio:
            print('Error: No se pueden poner más datos')
            return

        if isinstance(self, SenialCola):
            self._valores[self._cola] = valor
            self._cola = (self._cola + 1) % self._tamanio
        else:
            self._valores.append(valor)

        self._cantidad += 1

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

    def limpiar(self) -> None:
        """Vacía la señal por completo."""
        self._valores.clear()
        self._cantidad = 0

    def esta_vacia(self) -> bool:
        """
        Verifica si la señal no contiene valores.

        :return: True si la señal está vacía, False en caso contrario
        """
        return len(self._valores) == 0

    def obtener_valores(self) -> List[float]:
        """
        Retorna la lista de valores.

        :return: lista de valores de la señal
        """
        return self._valores

    def poner_valores(self, valores: List[float]) -> None:
        """
        Reemplaza la lista de valores de la señal.

        :param valores: lista de valores a asignar
        """
        self._valores = valores

    def sacar_valor(self) -> Any:
        """
        Extrae el último valor ingresado a la señal.

        :return: último valor ingresado, o None si la señal está vacía
        """
        if self._cantidad == 0:
            return None
        self._cantidad -= 1
        return self._valores.pop()


Senial = SenialLista


class SenialPila(SenialBase):
    """
    Señal digital con comportamiento de pila (LIFO).
    """

    def __init__(self, tamanio: int = 10):
        """
        Inicializa una nueva señal digital vacía.

        :param tamanio: tamaño máximo de la señal
        """
        super().__init__(tamanio)
        self._valores: List[float] = []

    def poner_valor(self, valor):
        """
        Agrega un nuevo valor al tope de la pila.

        :param valor: valor numérico a agregar a la señal
        """
        if self._cantidad >= self._tamanio:
            print('Error: No se pueden poner más datos')
            return
        self._valores.append(valor)
        self._cantidad += 1

    def sacar_valor(self) -> Any:
        """
        Extrae el último valor ingresado a la señal.

        :return: último valor ingresado, o None si la señal está vacía
        """
        if self._cantidad == 0:
            return None
        self._cantidad -= 1
        return self._valores.pop()

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

    def limpiar(self) -> None:
        """Vacía la señal por completo."""
        self._valores.clear()
        self._cantidad = 0


class SenialCola(Senial):
    """
    Señal digital con comportamiento de cola (FIFO).
    """

    def __init__(self, tamanio: int):
        """
        Inicializa la señal como un buffer circular de tamaño fijo.

        :param tamanio: tamaño de la cola
        """
        super().__init__(tamanio)
        self._cabeza = 0
        self._cola = 0
        self._valores = [None] * tamanio

    def sacar_valor(self) -> Any:
        """
        Extrae el primer valor ingresado a la señal.

        :return: primer valor ingresado, o None si la señal está vacía
        """
        if self._cantidad == 0:
            print('Error: No hay valores para sacar')
            return None
        valor = self._valores[self._cabeza]
        self._valores[self._cabeza] = None
        self._cabeza = (self._cabeza + 1) % self._tamanio
        self._cantidad -= 1
        return valor
