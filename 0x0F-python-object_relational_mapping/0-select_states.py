#!/usr/bin/python3
import MySQLdb
import sys
""" list all state"""
if __name__ = "__main__":

    db = MySQLdb.connect(user=sql.argv[1], passwd=sys.argv[2],
                     db=sys.argv[3], host='localhost', port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    states = cur.fetchall()
    for state in states:
        print(state)
    cursor.close()
    db.close()


