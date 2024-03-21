#!/usr/bin/python3
"""Script to add the State object "Louisiana" to the database"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Extract command-line arguments
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

    # Create State object for Louisiana
    new_state = State(name="Louisiana")

    # Add State object to the session and commit
    session.add(new_state)
    session.commit()

    # Print the new state's ID
    print(new_state.id)

    # Close session
    session.close()
