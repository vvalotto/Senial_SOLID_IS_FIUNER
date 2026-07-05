from setuptools import setup
import pathlib

HERE = pathlib.Path(__file__).parent
README_PATH = HERE / "README.md"
README = README_PATH.read_text(encoding="utf-8") if README_PATH.exists() else "Factory centralizado con configuración externa (DIP)"

setup(
    name="configurador",
    version="3.0.0",
    description="Factory centralizado que lee config.json y delega en los Factories especializados (DIP)",
    long_description=README,
    long_description_content_type="text/markdown",
    author="Victor Valotto",
    author_email="vvalotto@gmail.com",
    url="https://github.com/vvalotto/Senial_SOLID_IS_FIUNER",
    license="MIT",
    package_dir={"configurador": "."},
    packages=["configurador"],
    include_package_data=True,
    package_data={"configurador": ["config.json", "ejemplos/*.json"]},
    python_requires=">=3.8",
    install_requires=[
        "dominio-senial>=3.2.0",
        "adquisicion-senial>=3.1.0",
        "procesamiento-senial>=3.0.0",
        "presentacion-senial>=2.1.0",
        "persistidor-senial>=4.2.0",
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
    keywords="solid principles, dependency inversion, factory pattern, education",
    project_urls={
        "Bug Reports": "https://github.com/vvalotto/Senial_SOLID_IS_FIUNER/issues",
        "Source": "https://github.com/vvalotto/Senial_SOLID_IS_FIUNER",
    },
)
