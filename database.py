#!usr/bin/python

import sqlite3
import numpy as np
import io

def adapt_array(array):
    out = io.BytesIO()
    np.save(out, array)
    out.seek(0)
    return sqlite3.Binary(out.read())

def convert_array(text):
    out = io.BytesIO(text)
    out.seek(0)
    return np.load(out)


sqlite3.register_adapter(np.ndarray, adapt_array)

sqlite3.register_adapter("array", convert_array)

x = np.arrange(12).reshape(2,6)
conn = sqlite3.connect('maze.db');
conn.execute('''INSERT INTO MAZES(NAME) VALUES ''')


#https://stackoverflow.com/questions/18621513/python-insert-numpy-array-into-sqlite3-database


# print("Opened database successfully");
# #conn.execute('''DROP TABLE MAZES;''')
# conn.execute('''CREATE TABLE MAZES
#             (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
#              NAME TEXT NOT NULL,
#              TIME TEXT NOT NULL);''')
# print("Table created succesfully");
# conn.close();