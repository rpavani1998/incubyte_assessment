from mysql.connector import MySQLConnection, Error

class Mysql:
	def __init__(self, util):
		self.connection = self.db_connection(util.read_db_config())

	def db_connection(self, db_config):
		connection = None
		try:
			connection  = MySQLConnection(**db_config)
			if connection.is_connected():
				print('Connection established.')
			else:
				print('Unable to Establish Connection.')
		except Error as error:
			print("Failed to Establish Connection: ", error)
		return connection
	
	def close_connection(self):
		self.connection.close()


