#!/usr/bin/python3
import MySQLdb
import sys
mysql_username = sys.argv[1]
mysql_password = sys.argv[2]
database_name = sys.argv[3]
db = MySQLdb.connect(user=mysql_username, passwd=mysql_password,
                     db=database_name, host='localhost', port=3306)
cursor = db.cursor()
cursor.execute("SELECT * FROM states")
states = cursor.fetchall()
for state in states:
    print(state)

cursor.close()
db.close()


