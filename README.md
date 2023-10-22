[![CI](https://github.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Miniproject7/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Miniproject7/actions/workflows/cicd.yml)

IDS706_DataEngineering_BarbaraFlores_Miniproject7
## 📂 Package a Python Script into a Command-Line Tool

The objective of this miniproject is to package a Python command-line tool using setuptools, ensuring functionality and clear user guide creation, with optional communication with an external/internal database.

In this miniproject, the following activities were performed:

1. Package a Python script with setuptools or a similar tool
2. Include a user guide on how to install and use the tool
3. Include communication with an external or internal database (NoSQL, SQL, etc) 

## User Guide etl-tool 

The "etl-tool" is a command-line utility that allows you to perform Extract, Transform, and Load (ETL) processes on [world-small.csv](https://raw.githubusercontent.com/sejdemyr/sejdemyr.github.io/master/r-tutorials/basics/data/world-small.csv) database

This database was employed in the `"Practical Data Science"` class taught by Nick Eubank. This database contains information about some countries, their regions, and their values for `Polity IV` and `gdppcap08`.

- The `polityIV` variable in this dataset is an expert score for a country's authoritarianism. Traditionally, values of -10 represent extreme autocracies, while values of 10 denote consolidated liberal democracies. However, in this dataset, they have been rescaled to range from 0 to 20, where 0 represents an extreme autocracy, and 20 represents a consolidated liberal democracy.

- The variable `gdppcap08` represents the GDP per Capita values for countries in the year 2008.
data. This tool simplifies interactions with external or internal databases (SQL, NoSQL, etc.) and is designed to streamline common ETL tasks.

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

```python
pip install .
```
This will install the tool and its dependencies in your virtual environment.

## Running the Tool
Once installed, you can use the "etl-tool" from the command line. Here is an overview of how to use the tool:

```python
etl-tool
```

