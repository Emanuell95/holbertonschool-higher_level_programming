#!/usr/bin/python3
"""
Prints the first State object from the database hbtn_0e_6_usa using SQLAlchemy.
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
    
    # Fetch the first State object
    first_state = session.query(State).order_by(State.id).first()
    
    # Print the result or "Nothing" if the table is empty
    if first_state:
        print(f"{first_state.id}: {first_state.name}")
    else:
        print("Nothing")
    
    # Close the session
    session.close()
