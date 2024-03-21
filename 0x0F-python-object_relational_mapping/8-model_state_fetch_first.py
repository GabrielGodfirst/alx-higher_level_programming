#!/usr/bin/python3
"""Script to print the first State object from the database"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Database connection
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, db_name),
                           pool_pre_ping=True)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Query the first State object
    first_state = session.query(State).order_by(State.id).first()

    # Print the result
    if first_state:
        print("{}: {}".format(first_state.id, first_state.name))
    else:
        print("Nothing")

    # Close session
    session.close()
