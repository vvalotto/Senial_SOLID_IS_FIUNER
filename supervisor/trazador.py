"""
Módulo que define el contrato de trazabilidad.
"""
from abc import ABC, abstractmethod
from typing import Any


class BaseTrazador(ABC):
    """
    Contrato para la trazabilidad de eventos sobre una entidad.
    """

    @abstractmethod
    def trazar(self, entidad: Any, accion: str, mensaje: str) -> None:
        pass
