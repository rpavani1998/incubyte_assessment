import argparse
from collections import defaultdict
from util import Util
from mysqldb import Mysql
import threading
import pandas as pd

class HospitalDBSystem:
	def __init__(self, mysql):
		self.connection = mysql.connection

	def retrieve_country_names(self):
		cursor= self.connection.cursor()
		cursor.execute('SELECT * FROM Country')
		rows = cursor.fetchall()
		cursor.close()
		return {row[0] : row[1] for row in rows}
	
	def categorize_countrywise_data(self, data):
		countries = self.retrieve_country_names()
		data['DOB'] = pd.to_datetime(data['DOB'], format="%m%d%Y")
		countrywise_data = defaultdict(list)
		for i,row in data.iterrows():
			countrywise_data[countries[row.Country]].append(tuple(row.values[2:]))
		return countrywise_data	
	
	def create_table_if_not_exists(self, table, queryfile='createTable.sql'):
		cursor = self.connection.cursor()
		create_query = open(queryfile,'r').read().format('Table_'+ table)
		cursor.execute(create_query)
		cursor.close()
		
if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='DataLoad Parser')
	parser.add_argument('-f', '--filepath', action='store', help='DataFile Path', type=str, required=True)
	args = parser.parse_args()

	util = Util()
	mysql = Mysql(util)
	hdbs = HospitalDBSystem(mysql)
	data = util.read_file_data(args.filepath)
	categorized_data = hdbs.categorize_countrywise_data(data)	
	for country, data in categorized_data.items():
		hdbs.create_table_if_not_exists(country)
		cursor = mysql.connection.cursor()
		for row in data:
			insert_query = 'INSERT INTO Table_' + country + ' values' + str(row) + ';' 
			cursor.execute(insert_query)
		cursor.close()
	mysql.close_connection()		
		
	
	
