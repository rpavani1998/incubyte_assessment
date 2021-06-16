from configparser import ConfigParser
import pandas as pd

class Util:

	def read_db_config(self, filename='config.ini', section='mysqldb'):
		""" Read database configuration file and return a dictionary object
    		:param filename: name of the configuration file
    		:param section: section of database configuration
    		:return: a dictionary of database parameters
    		"""
	
		parser = ConfigParser()
		parser.read(filename)
        
		db = {}
		if parser.has_section(section):
			items = parser.items(section)
			for item in items:
				db[item[0]] = item[1]
		else:
			raise Exception('{0} not found in the {1} file'.format(section, filename))
		return db

	def read_file_data(self, file_path, delimiter='|'):
		""" Read data from file and return dataframe
                :param filepath: path to the data file
                :param delimiter: file delimiter
                :return: dataframe 
		"""

		df = pd.read_csv(file_path, delimiter=delimiter)
		return df
