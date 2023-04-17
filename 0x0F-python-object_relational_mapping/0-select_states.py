#!/usr/bin/python3
""" This is used to list states in database hbtn_0e_0_usa """
import MySQLdb
import sys



if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    item = db.curson()
    item.execute("SELECT * FROM states")
    values = item.fetchall()
    for value in values:
        print(value)
    item.close()
    db.close()
