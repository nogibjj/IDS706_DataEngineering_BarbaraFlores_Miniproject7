from setuptools import setup, find_packages

setup(
    name='EtlTool',  # Nombre de tu proyecto
    version='1.0',  # Versión de tu proyecto
    packages=find_packages(),  # Encuentra automáticamente todos los paquetes en tu proyecto
    install_requires=[
        # Lista de dependencias de tu proyecto
        # Por ejemplo:
        'numpy',
        'pandas',
        'sqlite3',
        'requests',
        'prettytable',
    ],
    entry_points={
        'console_scripts': [
            'etltool = EtlTool.main:main',  # Define un punto de entrada para tu programa principal
        ],
    },
    author='Barbara Flores',
    author_email='bpf17@duke.edu',
    description='An ETL (Extract, Transform, Load) tool written in Python',
    url='https://github.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Miniproject7',  # URL de tu repositorio en GitHub
)