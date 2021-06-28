import sqlite3
from sqlite3 import Error
from random import seed, randint
from time import time
from os import path

class Database:
	seed(time())
	__DB_LOCATION = path.join(path.realpath('.'),"data","typing.db")
	__CSV_LOCATION = path.join(path.realpath('.'),"data","words.csv")
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
		self.__init_words()
	
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
	def select_all_from_table(self, table):
		sql_command = """SELECT * FROM {}""".format(table)
		self.__cursor.execute(sql_command)
		return self.__cursor.fetchall()
	
	def select_random_word(self):
		return self.select_by_id(self.WORDS_TABLE, randint(1,1000))

	def select_by_id(self, table, id):
		"""
		fetches first matching id
		"""
		sql_command = """SELECT * FROM {} WHERE id=?""".format(table)
		rows = self.__cursor.execute(sql_command,(id,)).fetchone()
		return rows

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

	def __init_words(self):
		words = self.select_by_id(self.WORDS_TABLE, 1)
		if words is None:
			# parse csv
			with open(self.__CSV_LOCATION,'r') as reader:
				for id, line in enumerate(reader.readlines(), start=0):
					line = line.strip('\n\r')
					self.insert_data(self.WORDS_TABLE, self.WORDS_TABLE_COLS, (id,line))
					

	def insert_data(self, table, columns,data):
		"""inserts data into a table. will error if table does not exist
		:param table string TABLE NAME:
		:param columns COLUMNS corresponding to table. should be a string that is comma separated: 
		:param data two-dimensional list of data rows that corresponds with the selected table: 
		:returns newly inserted row's ID: """

		col_num = "?"+(",?"*columns.count(","))
		sql_command = """INSERT INTO {}({}) VALUES({})""".format(table, columns,col_num)
		self.__cursor.execute(sql_command, data)
		self.__conn.commit()
		


if __name__=="__main__":
	db = Database()
	random_word = db.select_random_word()[1]
	db.close()