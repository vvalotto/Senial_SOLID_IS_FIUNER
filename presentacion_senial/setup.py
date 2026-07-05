from setuptools import setup
import pathlib

HERE = pathlib.Path(__file__).parent
README_PATH = HERE / "README.md"
README = README_PATH.read_text(encoding="utf-8") if README_PATH.exists() else "Visualización de señales digitales"

setup(
    name="presentacion-senial",
    version="2.1.0",
    description="Visualizador de señales y fuentes de señal",
    long_description=README,
    long_description_content_type="text/markdown",
    author="Victor Valotto",
    author_email="vvalotto@gmail.com",
    url="https://github.com/vvalotto/Senial_SOLID_IS_FIUNER",
    license="MIT",
    package_dir={"presentacion_senial": "."},
    packages=["presentacion_senial"],
    python_requires=">=3.8",
    install_requires=[
        "dominio-senial>=3.2.0",
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Education",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Education",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords="solid principles, signal processing, visualization, education",
    project_urls={
        "Bug Reports": "https://github.com/vvalotto/Senial_SOLID_IS_FIUNER/issues",
        "Source": "https://github.com/vvalotto/Senial_SOLID_IS_FIUNER",
    },
)
