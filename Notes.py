import sqlite3 as sl
import os, datetime

Notes = {}

con = sl.connect('Notes.db')

sql = 'INSERT INTO NOTES (id, name, parent, note) values(?, ?, ?, ?)'
data = [
    1,
    'Test',
    'Test1',
    'does this work'
]

with con:
    data = con.execute("SELECT * FROM NOTES;")
    for i in data:
        print (f"{i[0]}")
    #con.execute("""
    #    CREATE TABLE IF NOT EXISTS NOTES (
    #        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    #        name TEXT,
    #        parent TEXT,
    #        note TEXT
    #    );
    #""")


#f=open("info.txt","w")