from setuptools import setup, find_packages

setup(
    name='etl-tool',
    version='0.1',
    author='Barbara Flores',
    author_email='bpf17@duke.edu',
    description='An ETL (Extract, Transform, Load) tool written in Python',
    long_description='''A Python ETL tool that facilitates the extraction, transformation, and loading of data. It uses requests and prettytable to perform various ETL operations.''',
    url='https://github.com/yourusername/etl-tool',
    packages=find_packages(exclude=['tests']),  # Exclude the 'tests' directory
    install_requires=[
        'requests',
        'prettytable',
        # Add other dependencies here
    ],
    entry_points={
        'console_scripts': [
            'etl-tool = etl_tool.main:main',
        ],
    },
    python_requires='>=3.6',
)