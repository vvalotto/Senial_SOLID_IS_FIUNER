#!/bin/bash
# install.sh - Instalación de Senial_SOLID_IS_FIUNER desde wheels ya buildeados
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(dirname "$SCRIPT_DIR")"
RELEASE_DIR="$ROOT_DIR/packaging/release"

GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[0;33m'
RED='\033[0;31m'
NC='\033[0m'

print_step() { echo -e "${BLUE}==>${NC} $1"; }
print_success() { echo -e "${GREEN}✓${NC} $1"; }
print_warning() { echo -e "${YELLOW}⚠${NC} $1"; }
print_error() { echo -e "${RED}✗${NC} $1"; }

check_python() {
    print_step "Verificando Python..."
    if ! command -v python3 &> /dev/null; then
        print_error "Python 3 no encontrado"
        exit 1
    fi
    print_success "Python $(python3 --version | cut -d' ' -f2) detectado"
}

check_wheels() {
    if [ ! -d "$RELEASE_DIR/wheels" ] || [ -z "$(ls -A "$RELEASE_DIR/wheels" 2>/dev/null)" ]; then
        print_error "No hay wheels en $RELEASE_DIR/wheels"
        print_warning "Ejecute primero: ./build/build_all.sh"
        exit 1
    fi
}

ask_venv() {
    echo ""
    echo "¿Desea instalar en un entorno virtual? (recomendado)"
    echo "  [Y] Sí - Crear entorno virtual 'senial_env'"
    echo "  [N] No - Instalar en el Python actual"
    read -p "Selección [Y/n]: " choice
    case "$choice" in n|N) return 1 ;; *) return 0 ;; esac
}

create_venv() {
    print_step "Creando entorno virtual 'senial_env'..."
    python3 -m venv "$ROOT_DIR/senial_env"
    source "$ROOT_DIR/senial_env/bin/activate"
    print_success "Entorno virtual creado y activado"
}

install_from_wheels() {
    print_step "Instalando paquetes desde wheels..."
    python3 -m pip install --upgrade pip --quiet

    for pkg in dominio_senial supervisor adquisicion_senial procesamiento_senial \
               presentacion_senial persistidor_senial configurador lanzador senial_solid_fiuner; do
        pip install "$RELEASE_DIR/wheels/${pkg}"*.whl --quiet
    done

    print_success "Todos los paquetes instalados"
}

setup_config() {
    print_step "Configurando directorio de trabajo..."
    mkdir -p ~/.senial_solid_fiuner
    if [ -f "$RELEASE_DIR/config/config.json" ]; then
        cp "$RELEASE_DIR/config/config.json" ~/.senial_solid_fiuner/config.json
        print_success "Configuración copiada a: ~/.senial_solid_fiuner/config.json"
    fi
    mkdir -p ~/.senial_solid_fiuner/datos_persistidos/{adquisicion,procesamiento,fuente_senial}
    print_success "Directorio de trabajo configurado"
}

verify_installation() {
    print_step "Verificando instalación..."
    python3 "$SCRIPT_DIR/verify_installation.py"
}

show_summary() {
    echo ""
    echo "================================================"
    print_success "Instalación completada"
    echo "================================================"
    echo ""
    echo "🚀 Ejecutar: senial-solid-fiuner"
    echo "   o: python -m lanzador.lanzador"
    echo ""
    echo "📁 Config de referencia: ~/.senial_solid_fiuner/config.json"
    echo "   (config.json real que usa el sistema: configurador/config.json"
    echo "    del paquete instalado — copiar el de referencia ahí si hace falta)"
    echo ""
}

main() {
    echo "================================================"
    echo "  Instalación de Senial_SOLID_IS_FIUNER"
    echo "================================================"
    echo ""

    check_python
    check_wheels

    if ask_venv; then
        create_venv
    fi

    install_from_wheels
    setup_config
    verify_installation
    show_summary
}

main
