import sqlite3 as sl
import os, datetime

Notes = {}
if __name__ == "__main__":
    con = sl.connect('Notes.db')

#f=open("info.txt","w")