from setuptools import setup
import pathlib

HERE = pathlib.Path(__file__).parent
README_PATH = HERE / "README.md"
README = README_PATH.read_text(encoding="utf-8") if README_PATH.exists() else "Interfaces segregadas de auditoría y trazabilidad"

setup(
    name="supervisor",
    version="1.0.0",
    description="Interfaces segregadas de supervisión: BaseAuditor y BaseTrazador",
    long_description=README,
    long_description_content_type="text/markdown",
    author="Victor Valotto",
    author_email="vvalotto@gmail.com",
    url="https://github.com/vvalotto/Senial_SOLID_IS_FIUNER",
    license="MIT",
    package_dir={"supervisor": "."},
    packages=["supervisor"],
    python_requires=">=3.8",
    install_requires=[],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Education",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Education",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords="solid principles, interface segregation, education",
    project_urls={
        "Bug Reports": "https://github.com/vvalotto/Senial_SOLID_IS_FIUNER/issues",
        "Source": "https://github.com/vvalotto/Senial_SOLID_IS_FIUNER",
    },
)
