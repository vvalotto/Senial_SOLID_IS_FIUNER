#!/usr/bin/env python3
"""
Verifica que las versiones declaradas en cada setup.py del proyecto sean
consistentes entre sí (que install_requires no pida una versión de un
paquete hermano más nueva que la que ese paquete realmente tiene).
"""
import re
import sys
from pathlib import Path
from typing import Dict, List, Optional


class Colors:
    GREEN = '\033[0;32m'
    BLUE = '\033[0;34m'
    RED = '\033[0;31m'
    NC = '\033[0m'


PAQUETES = [
    ("dominio_senial", "dominio-senial"),
    ("supervisor", "supervisor"),
    ("adquisicion_senial", "adquisicion-senial"),
    ("procesamiento_senial", "procesamiento-senial"),
    ("presentacion_senial", "presentacion-senial"),
    ("persistidor_senial", "persistidor-senial"),
    ("configurador", "configurador"),
    ("lanzador", "lanzador"),
]


class VerificadorVersiones:
    def __init__(self, root_dir: str = "."):
        self.root_dir = Path(root_dir).resolve()
        self.versiones: Dict[str, str] = {}
        self.dependencias: Dict[str, List[str]] = {}
        self.errores: List[str] = []

    @staticmethod
    def extraer_version(setup_path: Path) -> Optional[str]:
        if not setup_path.exists():
            return None
        contenido = setup_path.read_text(encoding="utf-8")
        match = re.search(r'version\s*=\s*["\']([^"\']+)["\']', contenido)
        return match.group(1) if match else None

    @staticmethod
    def extraer_dependencias(setup_path: Path) -> List[str]:
        if not setup_path.exists():
            return []
        contenido = setup_path.read_text(encoding="utf-8")
        match = re.search(r'install_requires\s*=\s*\[(.*?)\]', contenido, re.DOTALL)
        if not match:
            return []
        deps = []
        for linea in match.group(1).split('\n'):
            linea = linea.strip().strip(',').strip('"').strip("'")
            if linea and not linea.startswith('#'):
                deps.append(linea)
        return deps

    @staticmethod
    def comparar_versiones(v1: str, v2: str) -> int:
        p1 = [int(x) for x in v1.split('.')]
        p2 = [int(x) for x in v2.split('.')]
        for i in range(max(len(p1), len(p2))):
            a = p1[i] if i < len(p1) else 0
            b = p2[i] if i < len(p2) else 0
            if a != b:
                return 1 if a > b else -1
        return 0

    def verificar_paquetes(self) -> None:
        print(f"{Colors.BLUE}==>{Colors.NC} Verificando versiones de paquetes...\n")
        for dir_name, nombre_pypi in PAQUETES:
            setup_path = self.root_dir / dir_name / "setup.py"
            version = self.extraer_version(setup_path)
            if version:
                self.versiones[nombre_pypi] = version
                print(f"  {Colors.GREEN}✓{Colors.NC} {nombre_pypi}: v{version}")
            else:
                error = f"No se encontró versión en {setup_path}"
                self.errores.append(error)
                print(f"  {Colors.RED}✗{Colors.NC} {nombre_pypi}: {error}")
            deps = self.extraer_dependencias(setup_path)
            if deps:
                self.dependencias[nombre_pypi] = deps

    def verificar_dependencias(self) -> None:
        print(f"\n{Colors.BLUE}==>{Colors.NC} Verificando consistencia de dependencias...\n")
        for paquete, deps in self.dependencias.items():
            for dep in deps:
                match = re.match(r'([a-z-]+)>=([0-9.]+)', dep)
                if not match:
                    continue
                nombre_dep, version_requerida = match.groups()
                if nombre_dep not in self.versiones:
                    continue
                version_actual = self.versiones[nombre_dep]
                if self.comparar_versiones(version_actual, version_requerida) >= 0:
                    print(f"  {Colors.GREEN}✓{Colors.NC} {paquete} requiere "
                          f"{nombre_dep}>={version_requerida} (actual: {version_actual})")
                else:
                    error = (f"{paquete} requiere {nombre_dep}>={version_requerida} "
                             f"pero la versión actual es {version_actual}")
                    self.errores.append(error)
                    print(f"  {Colors.RED}✗{Colors.NC} {error}")

    def run(self) -> bool:
        print("=" * 60)
        print("  Verificación de versiones — Senial_SOLID_IS_FIUNER")
        print("=" * 60 + "\n")

        self.verificar_paquetes()
        self.verificar_dependencias()

        print("\n" + "=" * 60)
        if self.errores:
            print(f"{Colors.RED}✗ Verificación FALLÓ{Colors.NC}")
            for error in self.errores:
                print(f"  • {error}")
            print("=" * 60 + "\n")
            return False
        print(f"{Colors.GREEN}✓ Todas las versiones son consistentes{Colors.NC}")
        print("=" * 60 + "\n")
        return True


if __name__ == "__main__":
    sys.exit(0 if VerificadorVersiones().run() else 1)
