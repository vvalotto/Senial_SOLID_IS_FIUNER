"""
Módulo que define la clase Configurador.
"""
from dominio_senial import FactorySenial
from adquisicion_senial import BaseAdquisidor, FactoryAdquisidor
from procesamiento_senial import BaseProcesador, FactoryProcesador
from presentacion_senial import Visualizador
from persistidor_senial import BaseRepositorio, RepositorioSenial, RepositorioFuenteSenial, FactoryContexto

from configurador.cargador_config import CargadorConfig


class Configurador:
    """
    Configurador de la aplicación.

    Lee la configuración externa (config.json) y delega la creación de
    cada instancia concreta al Factory especializado correspondiente.
    Ninguna decisión de tipo concreto vive en este módulo.
    """

    _cargador = None

    @staticmethod
    def inicializar_configuracion(ruta_config=None):
        """
        Carga la configuración externa. Debe llamarse antes de crear componentes.

        :param ruta_config: ruta al archivo de configuración (None = config.json del módulo)
        """
        Configurador._cargador = CargadorConfig(ruta_config)
        Configurador._cargador.cargar()

    @staticmethod
    def crear_senial_adquisidor():
        """
        :return: señal configurada para el adquisidor
        """
        config = Configurador._cargador.obtener_config_senial_adquisidor()
        return FactorySenial.crear(config.get("tipo", "lista"), config)

    @staticmethod
    def crear_senial_procesador():
        """
        :return: señal configurada para el procesador
        """
        config = Configurador._cargador.obtener_config_senial_procesador()
        return FactorySenial.crear(config.get("tipo", "lista"), config)

    @staticmethod
    def crear_adquisidor() -> BaseAdquisidor:
        """
        :return: instancia de BaseAdquisidor configurada desde config.json
        """
        config = Configurador._cargador.obtener_config_adquisidor()
        senial = Configurador.crear_senial_adquisidor()
        return FactoryAdquisidor.crear(config.get("tipo", "archivo"), config, senial)

    @staticmethod
    def crear_procesador() -> BaseProcesador:
        """
        :return: instancia de BaseProcesador configurada desde config.json
        """
        config = Configurador._cargador.obtener_config_procesador()
        senial = Configurador.crear_senial_procesador()
        return FactoryProcesador.crear(config.get("tipo", "amplificador"), config, senial)

    @staticmethod
    def crear_visualizador():
        """
        :return: instancia de Visualizador
        """
        return Visualizador()

    @staticmethod
    def crear_repositorio_adquisicion() -> BaseRepositorio:
        """
        :return: RepositorioSenial configurado desde config.json para la señal adquirida
        """
        config = Configurador._cargador.obtener_config_contexto_adquisicion()
        contexto = FactoryContexto.crear(config.get("tipo", "pickle"), config)
        return RepositorioSenial(contexto)

    @staticmethod
    def crear_repositorio_procesamiento() -> BaseRepositorio:
        """
        :return: RepositorioSenial configurado desde config.json para la señal procesada
        """
        config = Configurador._cargador.obtener_config_contexto_procesamiento()
        contexto = FactoryContexto.crear(config.get("tipo", "pickle"), config)
        return RepositorioSenial(contexto)

    @staticmethod
    def crear_repositorio_fuente_senial() -> BaseRepositorio:
        """
        :return: RepositorioFuenteSenial configurado desde config.json
        """
        config = Configurador._cargador.obtener_config_contexto_fuente_senial()
        contexto = FactoryContexto.crear(config.get("tipo", "pickle"), config)
        return RepositorioFuenteSenial(contexto)
