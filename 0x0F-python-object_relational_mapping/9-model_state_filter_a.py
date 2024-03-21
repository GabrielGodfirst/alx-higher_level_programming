#!/usr/bin/python3
"""Script to list all State objects containing the letter 'a'"""

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

    # Query State objects containing the letter 'a'
    states_with_a = session.query(State).filter(
            State.name.like('%a%')).order_by(State.id).all()

    # Print the results
    for state in states_with_a:
        print("{}: {}".format(state.id, state.name))

    # Close session
    session.close()
