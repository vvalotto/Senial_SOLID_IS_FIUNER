from setuptools import setup, find_packages
import os


def read_long_description():
    here = os.path.abspath(os.path.dirname(__file__))
    readme_path = os.path.join(here, 'README.md')
    if os.path.exists(readme_path):
        with open(readme_path, encoding='utf-8') as f:
            return f.read()
    return "Sistema completo de procesamiento de señales con principios SOLID aplicados"


setup(
    name="senial-solid-fiuner",
    version="10.0.0",
    description="Sistema completo de procesamiento de señales con los 5 principios SOLID aplicados",
    long_description=read_long_description(),
    long_description_content_type="text/markdown",
    author="Victor Valotto",
    author_email="vvalotto@gmail.com",
    url="https://github.com/vvalotto/Senial_SOLID_IS_FIUNER",
    project_urls={
        "Bug Reports": "https://github.com/vvalotto/Senial_SOLID_IS_FIUNER/issues",
        "Documentation": "https://github.com/vvalotto/Senial_SOLID_IS_FIUNER/blob/main/README.md",
        "Source Code": "https://github.com/vvalotto/Senial_SOLID_IS_FIUNER",
    },
    license="MIT",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[
        "lanzador>=3.0.0",
    ],
    entry_points={
        "console_scripts": [
            "senial-solid-fiuner=lanzador.lanzador:ejecutar",
        ],
    },
    include_package_data=True,
    package_data={
        "senial_solid_fiuner": ["config/*.json"],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Education",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Education",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords="solid principles signal-processing architecture design-patterns education",
    zip_safe=False,
)
