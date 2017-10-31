#!usr/bin/python

import sqlite3
conn = sqlite3.connect('maze.db');
print("Opened database successfully");
#conn.execute('''DROP TABLE MAZES;''')
conn.execute('''CREATE TABLE MAZES
            (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
             NAME TEXT NOT NULL,
             TIME TEXT NOT NULL);''')
print("Table created succesfully");
conn.close();