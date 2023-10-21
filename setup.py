from setuptools import setup, find_packages

setup(
    name='etl-tool',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests',
        'prettytable',
        # Agrega otras dependencias aquí
    ],
    entry_points={
        'console_scripts': [
            'etl-tool = main:main',
        ],
    },
    python_requires='>=3.6',
)
