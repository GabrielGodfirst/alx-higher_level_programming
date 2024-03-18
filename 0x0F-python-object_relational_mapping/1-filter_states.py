#!/usr/bin/python3
"""
This script shows all the states with a name starting with N (upper N)
from the database
"""
import MySQLdb
from sys import argv

# code snippets executed when imported
if __name__ == '__main__':

    # Connects ot the database
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    # Enables multiple seperate working environments
    # from the same connection to the database.
    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE name\
                LIKE BINARY 'N%' ORDER BY id ASC")

    rows = cur.fetchall()
    for i in rows:
        print(i)
    # Mob up process
    cur.close()
    db.close()
