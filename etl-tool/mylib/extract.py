"""
We will use a 'small world' database from Nick Eubank's Class,
which is utilized for the 'Practical Data Science' class
"""
import os
import requests

def extract(url="https://raw.githubusercontent.com/nickeubank/practicaldatascience/master/Example_Data/world-small.csv", 
            file_path="etl-tool/data/WorldSmall.csv"):
    """Extract a URL to a file path"""
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    timeout = 100
    with requests.get(url, timeout=timeout) as r:
        with open(file_path, 'wb') as f:
            f.write(r.content)
    return file_path
