"""
Patrón Repository: separa la lógica de dominio de la infraestructura de
persistencia (Contexto), aplicando DIP mediante inyección de dependencias.
"""
from abc import ABC, abstractmethod
from typing import Any

from persistidor_senial.contexto import BaseContexto


class BaseRepositorio(ABC):
    """
    Contrato común para el acceso a la persistencia de una entidad.
    """

    def __init__(self, contexto: BaseContexto):
        self._contexto = contexto

    @abstractmethod
    def guardar(self, entidad: Any) -> None:
        pass

    @abstractmethod
    def obtener(self, id_entidad: str) -> Any:
        pass


class RepositorioSenial(BaseRepositorio):
    """
    Repositorio para gestionar la persistencia de señales.
    """

    def guardar(self, senial: Any) -> None:
        self._contexto.persistir(senial, str(senial.id))

    def obtener(self, id_senial: str) -> Any:
        return self._contexto.recuperar(id_senial)


class RepositorioFuenteSenial(BaseRepositorio):
    """
    Repositorio para gestionar la persistencia del catálogo de fuentes de señal.
    """

    def guardar(self, fuente: Any) -> None:
        self._contexto.persistir(fuente, str(fuente.id))

    def obtener(self, id_fuente: str) -> Any:
        return self._contexto.recuperar(id_fuente)
