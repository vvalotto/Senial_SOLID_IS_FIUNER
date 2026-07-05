"""
Patrón Repository: separa la lógica de dominio de la infraestructura de
persistencia (Contexto), aplicando DIP mediante inyección de dependencias.
"""
from abc import ABC, abstractmethod
from datetime import datetime
from typing import Any

from persistidor_senial.contexto import BaseContexto
from supervisor import BaseAuditor, BaseTrazador


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


class RepositorioSenial(BaseAuditor, BaseTrazador, BaseRepositorio):
    """
    Repositorio para gestionar la persistencia, auditoría y trazabilidad de señales.

    Declara explícitamente las tres capacidades que necesita, en vez de
    heredarlas todas de una única interfaz gorda.
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

    # Sin auditar(). Sin trazar(). Sin stubs. Sin mentiras.
