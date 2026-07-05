"""
Módulo que define el contrato de auditoría.
"""
from abc import ABC, abstractmethod
from typing import Any


class BaseAuditor(ABC):
    """
    Contrato para la auditoría de operaciones sobre una entidad.
    """

    @abstractmethod
    def auditar(self, entidad: Any, auditoria: str) -> None:
        pass
