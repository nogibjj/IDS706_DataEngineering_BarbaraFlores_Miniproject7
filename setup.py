from setuptools import setup, find_packages

setup(
    name='my_tool',
    version='0.1',
    packages=['my_tool'],
    install_requires=[
        # Lista de tus dependencias aquí
    ],
    entry_points={
        'console_scripts': [
            'my-tool = my_tool.mi_script:main',
        ],
    },
)