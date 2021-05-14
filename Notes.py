import sqlite3 as sl
import os, datetime

Notes = []



sql = 'INSERT INTO NOTES (id, name, parent, note) values(?, ?, ?, ?)'
Query = [
    5,
    'Test5',
    'Test1',
    'does this work'
]

con = sl.connect('Notes.db')

def Note_Retrieval(Note):
    with con:
        note = con.execute(f"SELECT * FROM NOTES WHERE name = '{Note}'")
    for i in note:
        print (i[1])
        print (i[3])
        Data_format(i[1], 1)

def Data_format(parent, loop):
    Children =[]
    for rows in range(len(Notes)):
        #sorts the data into, the points with no parents and collects them
        if Notes[rows][2] == parent:
            Children.append(Notes[rows][1])
    if len(Children) !=0:
        for  i in Children:
            print(" "*loop + i)
            Data_format(i, loop+1)
    elif len(Children)==0:
        #print(parent)
        return('')



with con:
    con.execute("""
        CREATE TABLE IF NOT EXISTS NOTES (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            parent TEXT,
            note TEXT
        );
    """)
    #initial data retrieval
    data = con.execute("SELECT * FROM NOTES")
    for i in data:
        Notes .append(i)

Output = Data_format('origin', 0)
#con.execute(sql, Query)

input = input("Which note would you like to view? ")
Note_Retrieval(input)