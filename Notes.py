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

def Data_format(parent):
    Children =[]
    for rows in range(len(Notes)):
        #sorts the data into, the points with no parents and collects them
        if Notes[rows][2] == parent:
            Children.append(Notes[rows][1])
    if len(Children) !=0:
        for  i in Children:
            print(i)
            Data_format(i)
    elif len(Children)==0:
        #print(parent)
        return('')

con = sl.connect('Notes.db')

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
    Output = Data_format('origin')
    #con.execute(sql, Query)
    


#f=open("info.txt","w")