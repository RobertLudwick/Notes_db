import sqlite3 as sl
import os, datetime

Notes = []



sql = 'INSERT INTO NOTES (name, parent, note) values(?, ?, ?)'
Query = []

con = sl.connect('Notes.db')

def Note_add():
    Parent = input("Pick a Parent ")
    Name = input("Name your Note ")
    Text= input("Write your note ")
    Query.append(Name)
    Query.append(Parent)
    Query.append(Text)
    with con:
        con.execute(sql, Query)
    

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


response = input("Which note would you like to view? ")
if response == "add":
    Note_add()
else:
    Note_Retrieval(input)