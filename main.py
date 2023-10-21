"""
ETL-Query script
"""

from mylib.extract import extract
from mylib.transform_load import load
from mylib.query import query

def main():
    # Extract
    print("Extrayendo datos...")
    extract()

    # Transform and load
    print("Transformando datos...")
    load()

    # Query
    print("Consultando datos...")
    query()

if __name__ == "__main__":
    main()