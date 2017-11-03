#!/usr/bin/python

import sqlite3

conn = None


def openConnection():
    conn = sqlite3.connect('maze.db')
    print("connection openend")

def insertImage():
    if (conn is not None):
        conn.execute("insert into test VALUES ")

    else:
        print("First open connection!")


def createDatabase():
    conn.execute('''CREATE TABLE mazes(
                  id INTEGER AUTOINCREMENT  )''')