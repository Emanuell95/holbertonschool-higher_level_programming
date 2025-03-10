#!/usr/bin/python3
"""
Changes the name of a State object in the database hbtn_0e_6_usa.
Updates the State where id = 2 to "New Mexico".
Takes 3 arguments: MySQL username, MySQL password, and database name.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./script.py <username> <password> <database>")
        sys.exit(1)

    # Get MySQL credentials from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Create engine to connect to MySQL database
    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}",
        pool_pre_ping=True
    )
    
    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # Query the State with id = 2
    state = session.query(State).filter_by(id=2).first()
    
    # Update the state's name if found
    if state:
        state.name = "New Mexico"
        session.commit()
    
    # Close the session
    session.close()
