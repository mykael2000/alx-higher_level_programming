#!/usr/bin/python3
"""
    Displays all values in the states table of hbtn_0e_0_usa
"""

import sys
import MySQLdb

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    item = conn.cursor()
    item.execute("SELECT * FROM states WHERE name LIKE BINARY `{}`" .format(sys.argv[4]))
    getter = item.fetchall()
    for get in getter:
        print(get)

    item.close() 
    conn.close()

