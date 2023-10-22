[![CI](https://github.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Miniproject7/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Miniproject7/actions/workflows/cicd.yml)

IDS706_DataEngineering_BarbaraFlores_Miniproject7
## 📂 Package a Python Script into a Command-Line Tool

The objective of this miniproject is to package a Python command-line tool using setuptools, ensuring functionality and clear user guide creation, with optional communication with an external/internal database.

In this miniproject, the following activities were performed:

1. Package a Python script with setuptools or a similar tool
2. Include a user guide on how to install and use the tool
3. Include communication with an external or internal database (NoSQL, SQL, etc)

## User Guide etl-tool 

This script is part of an Extract, Transform, Load (ETL) tool. It extracts data from a remote URL, transforms it, and loads it into a local SQLite database. The script provides functions for each ETL step, including extraction, transformation, and querying the database. It also includes functionality to update and query the loaded data. 

To run the complete ETL process, execute this script. It will perform the following steps:
1. Extract data from a URL and save it as 'WorldSmall.csv' in the 'EtlTool/data' directory.
2. Transform the extracted data and load it into a local SQLite database, creating the 'WorldSmallDB.db' file.
3. Perform various queries on the loaded data and display the results.

The script is a part of a larger tool and can be used independently or as part of a broader data processing pipeline.


### Table of Contents: 
1. Requirements
2. Installation
3. Usage
4. Examples

## Requirements
Ensure you have Python installed on your system. Additionally, this tool utilizes the following Python libraries, which will be automatically installed when following the installation instructions:

requests
prettytable

## Installation
To install the "etl-tool," follow these steps:

1. Clone this repository or download the package.
2. Navigate to the repository location in your terminal.
3. Run the following command to install "etl-tool":

```bash
pip install .
```

This will install the tool and its dependencies in your virtual environment.

## Running the Tool
Once installed, you can use the "etl-tool" from the command line. Here is an overview of how to use the tool:

```bash
etl-tool
```

