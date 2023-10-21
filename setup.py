from setuptools import setup

setup(
    name='your-package-name',
    version='0.1',
    packages=['your_package'],
    install_requires=[
        # List your dependencies here
    ],
    entry_points={
        'console_scripts': [
            'your-command-name = your_package.main:main',
        ],
    },
)