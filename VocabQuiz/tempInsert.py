import sqlite3

newConn = sqlite3.connect('tempVocab.db')

# newConn.execute('''CREATE TABLE VOCABULARY
#          (ID INT PRIMARY KEY     NOT NULL,
# 			  WORDS           TEXT    NOT NULL,
#          MEANING         TEXT    NOT NULL
#          );''')


def newData(id, words, meaning):
	newInsert = '''INSERT INTO VOCABULARY (ID, WORDS, MEANING) \
	      VALUES (?, ?, ?);'''
	dataTuple = (id, words, meaning)
	newConn.execute(newInsert, dataTuple)
	newConn.commit()