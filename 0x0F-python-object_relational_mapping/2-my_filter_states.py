#!/usr/bin/python3
"""
This script connects to a MySQL server and retrieves data from the states table
based on a given state name.
"""

import sys
import MySQLdb


def query_states():
    """
    Connects to a MySQL server and retrieves data from the states table based
    on a given state name.
    """
    # Extracting command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Establishing connection to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=password,
        db=database,
        port=3306
    )

    cursor = db.cursor()

    # Executing SQL query
    cursor.execute(
        "SELECT * FROM states WHERE name = %s ORDER BY id ASC", (state_name,)
    )
    data = cursor.fetchall()

    # Displaying results
    for row in data:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    query_states()
