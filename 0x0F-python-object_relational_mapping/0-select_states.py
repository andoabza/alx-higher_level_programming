#!/usr/bin/python3
from MySQLdb import _mysql
db = _mysql.connect("localhost", "root", "hbtn_0e_0_usa")
db.query("""SELECT * FROM states ORDER BY id ASC""")
r=db.use_result()
r.fetch_row()
