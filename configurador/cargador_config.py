"""
Módulo que define el cargador de configuración externa.
"""
import json
from pathlib import Path
from typing import Any, Dict


class CargadorConfig:
    """
    Lee y valida la configuración externa del sistema desde un archivo JSON.
    """

    def __init__(self, ruta_config: str = None):
        """
        :param ruta_config: ruta al archivo JSON de configuración. Si no se
            indica, se busca config.json en el mismo directorio que este módulo,
            sin importar desde dónde se ejecute el sistema.
        """
        if ruta_config is None:
            self._ruta_config = Path(__file__).parent / "config.json"
        else:
            self._ruta_config = Path(ruta_config)
        self._config = None

    def cargar(self) -> Dict[str, Any]:
        """Carga la configuración desde el archivo JSON."""
        with open(self._ruta_config, "r", encoding="utf-8") as archivo:
            self._config = json.load(archivo)
        return self._config

    def obtener_config_senial_adquisidor(self) -> Dict[str, Any]:
        if self._config is None:
            self.cargar()
        return self._config.get("senial_adquisidor", {"tipo": "lista", "tamanio": 10})

    def obtener_config_senial_procesador(self) -> Dict[str, Any]:
        if self._config is None:
            self.cargar()
        return self._config.get("senial_procesador", {"tipo": "lista", "tamanio": 10})

    def obtener_config_adquisidor(self) -> Dict[str, Any]:
        if self._config is None:
            self.cargar()
        return self._config.get("adquisidor", {"tipo": "consola", "num_muestras": 5})

    def obtener_config_procesador(self) -> Dict[str, Any]:
        if self._config is None:
            self.cargar()
        return self._config.get("procesador", {"tipo": "amplificador", "factor": 2.0})

    def obtener_config_contexto_adquisicion(self) -> Dict[str, Any]:
        if self._config is None:
            self.cargar()
        return self._config.get("contexto_adquisicion", {"tipo": "pickle", "recurso": "./datos_persistidos/adquisicion"})

    def obtener_config_contexto_procesamiento(self) -> Dict[str, Any]:
        if self._config is None:
            self.cargar()
        return self._config.get("contexto_procesamiento", {"tipo": "pickle", "recurso": "./datos_persistidos/procesamiento"})

    def obtener_config_contexto_fuente_senial(self) -> Dict[str, Any]:
        if self._config is None:
            self.cargar()
        return self._config.get("contexto_fuente_senial", {"tipo": "pickle", "recurso": "./datos_persistidos/fuente_senial"})
