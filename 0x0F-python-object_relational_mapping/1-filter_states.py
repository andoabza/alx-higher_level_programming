#!/usr/bin/python3
import MySQLdb
import sys
""" list all state based on id"""
if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', user=sys.argv[1], passwd=sys.argv[2],
                     db=sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%'")
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    db.close()
