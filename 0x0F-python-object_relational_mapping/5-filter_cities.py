#!/usr/bin/python3
import MySQLdb
import sys

user_name = sys.argv[1]
user_passwd = sys.argv[2]
db_name = sys.argv[3]
var = sys.argv[4]
db = MySQLdb.connect(user=user_name, password=user_passwd, db=db_name, host='localhost', port=3306)
cursor = db.cursor()
query = "SELECT cities.name FROM cities JOIN states ON cities.state_id = states.id WHERE states.name = %s ORDER BY cities.id ASC"
cursor.execute(query, (var,))
cities = cursor.fetchall()
citi = list(citi[0] for citi in cities)
print(*citi, sep=", ")
cursor.close()
db.close()

