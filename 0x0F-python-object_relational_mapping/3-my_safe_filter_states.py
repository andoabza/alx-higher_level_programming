#!/usr/bin/python3
""" print all name from database hbtn_0e_0_usa """
import MySQLdb
import sys
if __name__ == "__main__":
    if len(sys.argv[4]) < 9:
        var = sys.argv[4]
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                     db=sys.argv[3], host='localhost', port=3306)
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
