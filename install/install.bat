@echo off
REM install.bat - Instalación de Senial_SOLID_IS_FIUNER (Windows)

setlocal
set "ROOT_DIR=%~dp0.."
set "RELEASE_DIR=%ROOT_DIR%\packaging\release"

echo ================================================
echo   Instalacion de Senial_SOLID_IS_FIUNER
echo ================================================
echo.

python --version >nul 2>&1 || (
    echo ERROR: Python no encontrado
    exit /b 1
)

if not exist "%RELEASE_DIR%\wheels" (
    echo ERROR: No hay wheels en %RELEASE_DIR%\wheels
    echo Ejecute primero: build\build_all.bat
    exit /b 1
)

echo ==^> Instalando paquetes...
python -m pip install --upgrade pip --quiet

for %%p in (dominio_senial supervisor adquisicion_senial procesamiento_senial ^
            presentacion_senial persistidor_senial configurador lanzador senial_solid_fiuner) do (
    for %%f in ("%RELEASE_DIR%\wheels\%%p*.whl") do (
        python -m pip install "%%f" --quiet
    )
)
echo OK Paquetes instalados

echo ==^> Configurando...
if not exist "%USERPROFILE%\.senial_solid_fiuner" mkdir "%USERPROFILE%\.senial_solid_fiuner"
if exist "%RELEASE_DIR%\config\config.json" (
    copy "%RELEASE_DIR%\config\config.json" "%USERPROFILE%\.senial_solid_fiuner\" >nul
)
echo OK Configuracion completada

echo ==^> Verificando instalacion...
python "%~dp0verify_installation.py"

echo ================================================
echo OK Instalacion completada
echo ================================================
echo.
echo Ejecutar: senial-solid-fiuner
echo.

endlocal
