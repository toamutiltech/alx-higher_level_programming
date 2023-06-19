#!/usr/bin/python3
import MySQLdb
import sys

# Read the command-line arguments
username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]

#connent to Mysql server
conn = MySQLdb.connect(user=username, passwd=password, db=database)

#perform operation
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC")

#fetch and print result
query_rows = cur.fetchall()
for row in query_rows:
    print(row)

#close connection
cur.close()
conn.close()
