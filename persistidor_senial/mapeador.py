"""
Módulo que mapea entidades a una representación de texto y viceversa.
"""
from abc import ABCMeta, abstractmethod
from typing import Any


class Mapeador(metaclass=ABCMeta):
    """
    Contrato para mapear una entidad a texto y reconstruirla desde texto.
    """

    lista_tipos_base = ['int', 'str', 'float', 'bool']

    @staticmethod
    def tipo_dato(tipo: str, dato: str) -> Any:
        if tipo == 'int':
            return int(dato)
        elif tipo == 'float':
            return float(dato)
        elif tipo == 'bool':
            return bool(dato)
        elif tipo == 'str':
            return str(dato)
        return Mapeador.inferir_tipo(dato)

    @staticmethod
    def inferir_tipo(dato: str) -> Any:
        """Infiere el tipo cuando el campo destino vale None (no hay tipo previo que guíe la conversión)."""
        if dato == 'None':
            return None
        try:
            return int(dato)
        except ValueError:
            pass
        try:
            return float(dato)
        except ValueError:
            pass
        return dato

    @abstractmethod
    def ir_a_persistidor(self, entidad: Any) -> str:
        pass

    @abstractmethod
    def venir_desde_persistidor(self, entidad: Any, entidad_mapeada: str) -> Any:
        pass


class MapeadorArchivo(Mapeador):
    """
    Mapeador ad-hoc para persistencia en archivo de texto, campo a campo.
    """

    def ir_a_persistidor(self, entidad: Any) -> str:
        """Serializa los campos de la entidad a un texto, una línea por campo."""
        lineas = []
        for atributo, valor in entidad.__dict__.items():
            if isinstance(valor, list):
                for indice, elemento in enumerate(valor):
                    lineas.append(f"{atributo}>{indice}:{elemento}")
            else:
                lineas.append(f"{atributo}:{valor}")
        return '\n'.join(lineas) + '\n'

    def venir_desde_persistidor(self, entidad: Any, entidad_mapeada: str) -> Any:
        """Reconstruye los campos de la entidad a partir del texto serializado."""
        for linea in entidad_mapeada.strip().split('\n'):
            if not linea:
                continue
            clave, _, valor = linea.partition(':')
            if '>' in clave:
                atributo, indice_str = clave.split('>')
                if atributo in entidad.__dict__ and isinstance(entidad.__dict__[atributo], list):
                    lista = entidad.__dict__[atributo]
                    indice = int(indice_str)
                    while len(lista) <= indice:
                        lista.append(None)
                    lista[indice] = float(valor)
            elif clave in entidad.__dict__:
                tipo = entidad.__dict__[clave].__class__.__name__
                entidad.__dict__[clave] = Mapeador.tipo_dato(tipo, valor)
        return entidad
