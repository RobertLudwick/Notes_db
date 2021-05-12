#Write your own Queries in Query.txt and execute them by running this file
# For testing purposes only

import sqlite3 as sl

con = sl.connect('Notes.db')

q = open("Query.txt", "r")
sql = q.read()
q.close()

with con:
    data = con.execute(sql)
    for i in data:
        print (i)