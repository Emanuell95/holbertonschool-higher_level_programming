#!/usr/bin/python3
"""
Prints the State object with the name passed as an argument from the database hbtn_0e_6_usa.
Takes 4 arguments: MySQL username, MySQL password, database name, and state name to search.
Ensures safety from SQL injection.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: ./script.py <username> <password> <database> <state name>")
        sys.exit(1)

    # Get MySQL credentials and state name from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Create engine to connect to MySQL database
    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}",
        pool_pre_ping=True
    )
    
    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # Query for the state using a parameterized filter
    state = session.query(State).filter(State.name == state_name).first()
    
    # Print the state's id or "Not found" if it does not exist
    if state:
        print(state.id)
    else:
        print("Not found")
    
    # Close the session
    session.close()
