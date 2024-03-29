#!/usr/bin/python3
""" This is used to list states in database hbtn_0e_0_usa """
import MySQLdb
import sys



if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states")
    values = cur.fetchall()
    for value in values:
        print(value)
    cur.close()
    conn.close()
