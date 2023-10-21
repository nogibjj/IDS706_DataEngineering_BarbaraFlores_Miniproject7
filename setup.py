from setuptools import setup, find_packages

setup(
    name="EtlTool",
    version="0.1",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "etl-tool = EtlTool.main:main",
        ],
    },
    install_requires=[
        "requests",
        #"sqlite3",
        "prettytable",
    ],
    author="Barbara Flores",
    author_email="bpf17@duke.edu",
    description="Herramienta de ETL",
)
