"""
Transforms and Loads data into the local SQLite3 database
"""
import sqlite3
import csv
import os

def load(dataset="etl-tool/data/WorldSmall.csv"):
    """Transforms and Loads data into the local SQLite3 database"""

    # Imprime el directorio de trabajo actual y la ruta completa
    print(os.getcwd())

    with open(dataset, 'r', encoding='utf-8', newline='') as file:
        payload = csv.reader(file, delimiter=',')

        db_path = "etl-tool/data/WorldSmallDB.db"
        conn = sqlite3.connect(db_path)
        c = conn.cursor()

        c.execute("DROP TABLE IF EXISTS WorldSmallDB")
        c.execute("CREATE TABLE WorldSmallDB (country, region, gdppcap08, polityIV)")
        
        data = list(payload)
        
        for _, row in enumerate(data):
            country = row[0]
            region = row[1]
            gdppcap08 = row[2]
            polityIV = row[3]
            
            c.execute("INSERT INTO WorldSmallDB VALUES (?, ?, ?, ?)", (country, region, gdppcap08, polityIV))

        conn.commit()
        conn.close()

    return "WorldSmallDB.db"
