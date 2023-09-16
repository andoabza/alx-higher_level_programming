#!/usr/bin/python3
""" print id, name of cities and state on db hbtn_0e_4_usa """
import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                     db=sys.argv[3], host='localhost', port=3306)
    cursor = db.cursor()
    query = ("""SELECT cities.id, cities.name, states.name FROM cities INNER JOIN states ON cities.state_id = states.id ORDER BY id ASC""")
    cursor.execute(query)
    cities = cursor.fetchall()
    for citie in cities:
        print(citie)
    cursor.close()
    db.close()
