#!/usr/bin/python3

"""
This script list all the tables in database hbtn_0e_0_usa.
"""

import MySQLdb
from sys import argv


def list_states():
    """
    Connects to the MySQL database and lists all states.

    Args:
        None

    Returns:
        None
    """
    # The code should run when imported
    if __name__ == '__main__':

        # this part connects to the database
        db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                             passwd=argv[2], db=argv[3])

        # provides the ability for multiple separate working environments
        # from the same connection to the database.
        cur = db.cursor()
        cur.execute("SELECT * FROM states")

        rows = cur.fetchall()
        for i in rows:
            print(i)
        # Clean up process
        cur.close()
        db.close()


if __name__ == '__main__':
    list_states()
