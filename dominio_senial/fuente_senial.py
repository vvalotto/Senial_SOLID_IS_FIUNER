"""
Módulo que define la entidad FuenteSenial.
"""
from typing import Any


class FuenteSenial:
    """
    Representa el origen de una señal (sensor, archivo histórico, etc.).
    """

    def __init__(self, nombre: str = '', descripcion: str = ''):
        self._id = None
        self._nombre = nombre
        self._descripcion = descripcion

    @property
    def id(self) -> Any:
        return self._id

    @id.setter
    def id(self, valor) -> None:
        self._id = valor

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, valor: str) -> None:
        self._nombre = valor

    @property
    def descripcion(self) -> str:
        return self._descripcion

    @descripcion.setter
    def descripcion(self, valor: str) -> None:
        self._descripcion = valor
