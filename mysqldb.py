from mysql.connector import MySQLConnection, Error

class Mysql:
	def __init__(self, util):
		#Calling db_connection method, passsing the db properties read from the config.ini file, under mysqldb section
		self.connection = self.db_connection(util.read_db_config())

	def db_connection(self, db_config):
		""" Connect to MySQL database
		:param db_config: dictonary with database configuration
		:return: connection
		"""
		connection = None
		try:
			connection  = MySQLConnection(**db_config)
			if connection.is_connected():
			#	print('Connection established.')
			else:
				print('Unable to Establish Connection.')
		except Error as error:
			print("Failed to Establish Connection: ", error)
		return connection
	
	def close_connection(self):
		#Close Mysql Connection
		self.connection.close()


