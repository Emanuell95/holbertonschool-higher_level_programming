#!/usr/bin/python3
"""
Defines a State class that links to the MySQL table `states`.
Uses SQLAlchemy for ORM mapping.
"""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

# Create the base class for ORM
Base = declarative_base()


class State(Base):
    """State class that represents the `states` table in MySQL."""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)


if __name__ == "__main__":
    # Example connection string (replace username, password, and db_name accordingly)
    engine = create_engine("mysql+mysqldb://username:password@localhost:3306/db_name")
    
    # Create tables in the database
    Base.metadata.create_all(engine)
