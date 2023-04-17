#!/usr/bin/python3

""" Lists all states with a name starting with N  """

import MySQLdb
import sys

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id")
    lists = cur.fetchall()
    for list in lists:
        print(list)
    cur.close()
    conn.close()
