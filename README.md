# incubyte_assessment

Please read Data Engineer Assessment.pdf for assessment details.

Requirements:

To run the code following installations are required

- *MySQL*
- *Python3*

To install the required python libraries, run

    pip3 install -r requirements.txt
    
    
Maintaining a Country Table to hold code and name for each country.

    mysql -u root -p < country.sql
  

When this command is executed the Country table is craeted and sample data is inserted.
For any new country in data, record needs to be inserted in this table. Here name will be the name included in the Countrywise table name (Table_<table_name>)

Update the mysqldb configuration in config.ini file

Sample datafile - sample_data.txt

Executing the script

    python3 loadData.py -f <datafile>
    
    python3 loadData.py -f sample_data.txt
    
    
Data will be inserted into respective Country Table.
