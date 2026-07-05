@echo off
REM build_all.bat - Build de todos los paquetes de Senial_SOLID_IS_FIUNER (Windows)

setlocal enabledelayedexpansion
set "ROOT_DIR=%~dp0.."
set "RELEASE_DIR=%ROOT_DIR%\packaging\release"

echo ================================================
echo   Build de Senial_SOLID_IS_FIUNER
echo ================================================
echo.

python --version >nul 2>&1 || (
    echo ERROR: Python no encontrado
    exit /b 1
)

echo ==^> Instalando herramientas...
python -m pip install --upgrade pip setuptools wheel build --quiet

echo ==^> Verificando versiones...
python "%ROOT_DIR%\build\verify_versions.py" || exit /b 1

echo ==^> Limpiando builds anteriores...
if exist "%RELEASE_DIR%" rmdir /s /q "%RELEASE_DIR%"

echo ==^> Creando estructura...
mkdir "%RELEASE_DIR%\wheels"
mkdir "%RELEASE_DIR%\source"
mkdir "%RELEASE_DIR%\config"

goto :main

:build_package
set "package_dir=%~1"
echo ==^> Building %package_dir%...
cd "%ROOT_DIR%\%package_dir%"
python -m build || exit /b 1
if exist "dist\*.whl" copy "dist\*.whl" "%RELEASE_DIR%\wheels\" >nul
if exist "dist\*.tar.gz" copy "dist\*.tar.gz" "%RELEASE_DIR%\source\" >nul
echo OK %package_dir% built
cd "%ROOT_DIR%"
goto :eof

:main
call :build_package "dominio_senial"
call :build_package "supervisor"
call :build_package "adquisicion_senial"
call :build_package "procesamiento_senial"
call :build_package "presentacion_senial"
call :build_package "persistidor_senial"
call :build_package "configurador"
call :build_package "lanzador"
call :build_package "packaging\metapackage"

echo ==^> Copiando archivos adicionales...
copy "%ROOT_DIR%\configurador\config.json" "%RELEASE_DIR%\config\" >nul 2>nul
copy "%ROOT_DIR%\README.md" "%RELEASE_DIR%\" >nul 2>nul
copy "%ROOT_DIR%\LICENSE" "%RELEASE_DIR%\" >nul 2>nul

echo ================================================
echo OK Build completado
echo ================================================

endlocal
