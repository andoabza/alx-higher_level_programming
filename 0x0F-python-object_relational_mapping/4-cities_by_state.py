#!/usr/bin/python3
import sys
import MySQLdb

mysql_username = sys.argv[1]
mysql_password = sys.argv[2]
db_name = sys.argv[3]
db = MySQLdb.connect(user=mysql_username, passwd=mysql_password,
                     db=db_name, host='localhost', port=3306)
cursor = db.cursor()
query = ("SELECT cities.id, cities.name, states.name FROM cities INNER JOIN states ON cities.state_id = states.id ORDER BY id ASC")
cursor.execute(query)
cities = cursor.fetchall()
for citie in cities:
    print(citie)
cursor.close()
db.close()
