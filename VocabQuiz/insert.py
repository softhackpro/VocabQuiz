import sqlite3

conn = sqlite3.connect('Vocabulary.db')

# conn.execute('''CREATE TABLE VOCABULARY
#          (ID INT PRIMARY KEY     NOT NULL,
# 			  WORDS           TEXT    NOT NULL,
#          MEANING         TEXT    NOT NULL
#          );''')

def insertData(id, words, meaning):
	newInsert = '''INSERT INTO VOCABULARY (ID, WORDS, MEANING) \
	      VALUES (?, ?, ?);'''
	dataTuple = (id, words, meaning)
	conn.execute(newInsert, dataTuple)
	conn.commit()