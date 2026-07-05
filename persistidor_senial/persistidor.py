"""
Módulo con estrategias de persistencia para entidades del dominio.
"""
import importlib
import os
import pickle
from abc import ABC, abstractmethod
from typing import Any, Optional

from persistidor_senial.mapeador import MapeadorArchivo


class BasePersistidor(ABC):
    """
    Contrato común para cualquier estrategia de persistencia.
    """

    def __init__(self, recurso: str):
        self._recurso = recurso
        if not os.path.isdir(recurso):
            os.makedirs(recurso)

    @property
    def recurso(self) -> str:
        return self._recurso

    @abstractmethod
    def persistir(self, entidad: Any, nombre_entidad: str) -> None:
        pass

    @abstractmethod
    def recuperar(self, id_entidad: str) -> Optional[Any]:
        pass


class PersistidorPickle(BasePersistidor):
    """
    Persiste entidades de forma binaria, usando serialización pickle.
    """

    def persistir(self, entidad: Any, nombre_entidad: str) -> None:
        ubicacion = os.path.join(self._recurso, f"{nombre_entidad}.pickle")
        with open(ubicacion, "wb") as archivo:
            pickle.dump(entidad, archivo)

    def recuperar(self, id_entidad: str) -> Optional[Any]:
        ubicacion = os.path.join(self._recurso, f"{id_entidad}.pickle")
        with open(ubicacion, "rb") as archivo:
            return pickle.load(archivo)


class PersistidorArchivo(BasePersistidor):
    """
    Persiste entidades en un archivo de texto ad-hoc, campo a campo.
    """

    def persistir(self, entidad: Any, nombre_entidad: str) -> None:
        tipo_clase = f"__class__:{type(entidad).__module__}.{type(entidad).__name__}\n"
        mapeador = MapeadorArchivo()
        contenido = tipo_clase + mapeador.ir_a_persistidor(entidad)
        ubicacion = os.path.join(self._recurso, f"{nombre_entidad}.dat")
        with open(ubicacion, "w", encoding="utf-8") as archivo:
            archivo.write(contenido)

    def recuperar(self, id_entidad: str) -> Optional[Any]:
        ubicacion = os.path.join(self._recurso, f"{id_entidad}.dat")
        with open(ubicacion, "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()

        tipo_info = lineas[0].strip().split(':', 1)[1]
        modulo_nombre, clase_nombre = tipo_info.rsplit('.', 1)
        modulo = importlib.import_module(modulo_nombre)
        clase = getattr(modulo, clase_nombre)
        entidad = clase()

        mapeador = MapeadorArchivo()
        return mapeador.venir_desde_persistidor(entidad, ''.join(lineas[1:]))
