from setuptools import setup
import pathlib

HERE = pathlib.Path(__file__).parent
README_PATH = HERE / "README.md"
README = README_PATH.read_text(encoding="utf-8") if README_PATH.exists() else "Persistencia de entidades del dominio (Repository Pattern)"

setup(
    name="persistidor-senial",
    version="4.2.0",
    description="Persistencia con Repository Pattern (Contexto/Repositorio) y FactoryContexto",
    long_description=README,
    long_description_content_type="text/markdown",
    author="Victor Valotto",
    author_email="vvalotto@gmail.com",
    url="https://github.com/vvalotto/Senial_SOLID_IS_FIUNER",
    license="MIT",
    package_dir={"persistidor_senial": "."},
    packages=["persistidor_senial"],
    python_requires=">=3.8",
    install_requires=[
        "supervisor>=1.0.0",
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
    keywords="solid principles, repository pattern, persistence, education",
    project_urls={
        "Bug Reports": "https://github.com/vvalotto/Senial_SOLID_IS_FIUNER/issues",
        "Source": "https://github.com/vvalotto/Senial_SOLID_IS_FIUNER",
    },
)
