#!/bin/bash
# build_all.sh - Build de todos los paquetes de Senial_SOLID_IS_FIUNER
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(dirname "$SCRIPT_DIR")"
RELEASE_DIR="$ROOT_DIR/packaging/release"

GREEN='\033[0;32m'
BLUE='\033[0;34m'
RED='\033[0;31m'
NC='\033[0m'

print_step() { echo -e "${BLUE}==>${NC} $1"; }
print_success() { echo -e "${GREEN}✓${NC} $1"; }

PAQUETES=(dominio_senial supervisor adquisicion_senial procesamiento_senial
          presentacion_senial persistidor_senial configurador lanzador
          packaging/metapackage)

check_build_tools() {
    print_step "Verificando herramientas de build..."
    python3 -m pip install --upgrade pip setuptools wheel build --quiet
    print_success "Herramientas listas"
}

verify_versions() {
    print_step "Verificando versiones..."
    python3 "$SCRIPT_DIR/verify_versions.py" || exit 1
}

clean_previous_build() {
    print_step "Limpiando builds anteriores..."
    for dir in "${PAQUETES[@]}"; do
        rm -rf "$ROOT_DIR/$dir/dist" "$ROOT_DIR/$dir/build" "$ROOT_DIR/$dir"/*.egg-info
    done
    rm -rf "$RELEASE_DIR"
    print_success "Limpieza completada"
}

create_release_structure() {
    print_step "Creando estructura de release..."
    mkdir -p "$RELEASE_DIR"/{wheels,source,config}
    print_success "Estructura creada en $RELEASE_DIR"
}

build_package() {
    local package_dir=$1
    print_step "Building $package_dir..."
    (cd "$ROOT_DIR/$package_dir" && python3 -m build --outdir "$ROOT_DIR/$package_dir/dist") || exit 1
    cp "$ROOT_DIR/$package_dir"/dist/*.whl "$RELEASE_DIR/wheels/" 2>/dev/null || true
    cp "$ROOT_DIR/$package_dir"/dist/*.tar.gz "$RELEASE_DIR/source/" 2>/dev/null || true
    print_success "$package_dir built"
}

main() {
    echo "================================================"
    echo "  Build de Senial_SOLID_IS_FIUNER"
    echo "================================================"
    echo ""

    check_build_tools
    verify_versions
    clean_previous_build
    create_release_structure

    echo ""
    for pkg in "${PAQUETES[@]}"; do
        build_package "$pkg"
    done

    print_step "Copiando archivos adicionales..."
    cp "$ROOT_DIR/configurador/config.json" "$RELEASE_DIR/config/" 2>/dev/null || true
    cp "$ROOT_DIR/README.md" "$RELEASE_DIR/" 2>/dev/null || true
    cp "$ROOT_DIR/LICENSE" "$RELEASE_DIR/" 2>/dev/null || true
    print_success "Archivos copiados"

    echo ""
    echo "================================================"
    print_success "Build completado"
    echo "================================================"
    echo "📦 Wheels: $(ls -1 "$RELEASE_DIR"/wheels/*.whl 2>/dev/null | wc -l | tr -d ' ')"
    echo "📦 Source: $(ls -1 "$RELEASE_DIR"/source/*.tar.gz 2>/dev/null | wc -l | tr -d ' ')"
    echo "📁 Ubicación: $RELEASE_DIR"
}

main
