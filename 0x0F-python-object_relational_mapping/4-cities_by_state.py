#!/usr/bin/python3
"""
Code snippet that lists all cities from the database hbtn_0e_4_usa
"""
import MySQLdb
from sys import argv

# executes when imported
if __name__ == '__main__':

    # Connections to the database
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities\
                INNER JOIN states ON cities.state_id = states.id\
                ORDER BY cities.id ASC")

    rows = cur.fetchall()
    for i in rows:
        print(i)
    # Clean up process
    cur.close()
    db.close()
