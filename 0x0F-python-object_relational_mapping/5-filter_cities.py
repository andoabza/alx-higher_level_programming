#!/usr/bin/python3
""" print all name from database """
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], password=sys.argv[2], db=sys.argv[3], host='localhost', port=3306)
    cursor = db.cursor()
    query = ("""SELECT cities.name FROM cities JOIN states ON cities.state_id = states.id WHERE states.name = %s ORDER BY cities.id ASC""")
    cursor.execute(query, (sys.argv[4],))
    cities = cursor.fetchall()
    citi = list(citi[0] for citi in cities)
    print(*citi, sep=", ")
    cursor.close()
    db.close()

