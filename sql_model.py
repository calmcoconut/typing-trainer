import sqlite3
from sqlite3 import Error
from os import path

class Database:
	__DB_LOCATION = path.join(path.realpath('.'),"data","typing.db")
	__create_word_table = """CREATE TABLE IF NOT EXISTS words (
		id integer PRIMARY KEY,
		name text NOT NULL
	);"""
	WORDS_TABLE = "words"
	WORDS_TABLE_COLS = "id, name"

	def __init__(self):
		self.__conn = self.__create_connection(self.__DB_LOCATION)
		self.__cursor = self.__conn.cursor()
		self.__create_table()
	
	def __create_connection(self, db_file):
		"""connect to db path"""
		conn = None
		try:
			conn = sqlite3.connect(db_file)
			print(sqlite3.version)
		except Error as e:
			print(e)
		finally:
			return conn
	def select_by_id(self, table, id):
		sql_command = """SELECT * FROM {} WHERE {};"""
		pass

	def select_by_custom(self, table, condition):
		pass

	def close(self):
		self.__conn.close()
	
	def __create_table(self):
		try:
			self.__cursor.execute(
			self.__create_word_table
			)
		except Error as e:
			print(e)
	def insert_data(self, table, columns,data):
		"""inserts data into a table. will error if table does not exist
		:param table string TABLE NAME:
		:param columns COLUMNS corresponding to table. should be a string that is comma separated: 
		:param data two-dimensional list of data rows that corresponds with the selected table: 
		:returns newly inserted row's ID: """

		col_num = "?"+(",?"*columns.count(","))
		sql_command = """INSERT INTO {}({}) VALUES({})""".format(table, columns,col_num)
		for row in data:
			self.__cursor.execute(sql_command, row)
		self.__conn.commit()
		


if __name__=="__main__":
	db = Database()
	db.insert_data(db.WORDS_TABLE, db.WORDS_TABLE_COLS, [(1,"hello")])