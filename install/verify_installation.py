#!/usr/bin/env python3
"""Verifica que los 8 paquetes de Senial_SOLID_IS_FIUNER estén instalados e importables."""
import sys

COMPONENTES = [
    'dominio_senial',
    'supervisor',
    'adquisicion_senial',
    'procesamiento_senial',
    'presentacion_senial',
    'persistidor_senial',
    'configurador',
    'lanzador',
]


def verificar() -> int:
    print("=" * 60)
    print("  Verificación de instalación — Senial_SOLID_IS_FIUNER")
    print("=" * 60)
    print()

    errores = 0
    for componente in COMPONENTES:
        try:
            __import__(componente)
            print(f"✓ {componente}")
        except ImportError as e:
            print(f"✗ {componente} - ERROR: {e}")
            errores += 1

    print()
    print("=" * 60)
    if errores == 0:
        print("✓ Todos los componentes instalados correctamente")
        return 0
    print(f"✗ {errores} componente(s) con errores")
    return 1


if __name__ == "__main__":
    sys.exit(verificar())
