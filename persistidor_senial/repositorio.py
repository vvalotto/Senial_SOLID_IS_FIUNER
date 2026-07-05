"""
Patrón Repository: separa la lógica de dominio de la infraestructura de
persistencia (Contexto), aplicando DIP mediante inyección de dependencias.

⚠️ Violación ISP intencional: BaseRepositorio obliga a todo repositorio a
implementar auditar()/trazar(), aunque no todos los necesiten.
"""
from abc import ABC, abstractmethod
from datetime import datetime
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

    @abstractmethod
    def auditar(self, entidad: Any, auditoria: str) -> None:
        pass

    @abstractmethod
    def trazar(self, entidad: Any, accion: str, mensaje: str) -> None:
        pass


class RepositorioSenial(BaseRepositorio):
    """
    Repositorio para gestionar la persistencia, auditoría y trazabilidad de señales.
    """

    def guardar(self, senial: Any) -> None:
        self._contexto.persistir(senial, str(senial.id))

    def obtener(self, id_senial: str) -> Any:
        return self._contexto.recuperar(id_senial)

    def auditar(self, senial: Any, auditoria: str) -> None:
        with open('auditor.log', 'a', encoding='utf-8') as archivo:
            archivo.write(f'Señal ID: {senial.id} | {datetime.now()} | {auditoria}\n')

    def trazar(self, senial: Any, accion: str, mensaje: str) -> None:
        with open('logger.log', 'a', encoding='utf-8') as archivo:
            archivo.write(f'Señal ID: {senial.id} | {datetime.now()} | {accion} | {mensaje}\n')


class RepositorioFuenteSenial(BaseRepositorio):
    """
    Repositorio para gestionar la persistencia del catálogo de fuentes de señal.
    """

    def guardar(self, fuente: Any) -> None:
        self._contexto.persistir(fuente, str(fuente.id))

    def obtener(self, id_fuente: str) -> Any:
        return self._contexto.recuperar(id_fuente)

    def auditar(self, fuente: Any, auditoria: str) -> None:
        raise NotImplementedError("RepositorioFuenteSenial no soporta auditoría")

    def trazar(self, fuente: Any, accion: str, mensaje: str) -> None:
        raise NotImplementedError("RepositorioFuenteSenial no soporta trazabilidad")
