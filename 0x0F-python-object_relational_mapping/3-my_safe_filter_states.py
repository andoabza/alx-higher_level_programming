#!/usr/bin/python3
import MySQLdb
import sys
mysql_username = sys.argv[1]
mysql_password = sys.argv[2]
database_name = sys.argv[3]   
if len(sys.argv[4]) < 9:
    var = sys.argv[4]

db = MySQLdb.connect(user=mysql_username, passwd=mysql_password,
                     db=database_name, host='localhost', port=3306)
cursor = db.cursor()
try:
    query = "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY id ASC".format(var)
    cursor.execute(query)
    states = cursor.fetchall()
    for state in states:
        print(state)
except:
    pass
cursor.close()
db.close()
