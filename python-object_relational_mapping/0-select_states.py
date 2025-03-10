#!/usr/bin/python3
"""
Listing all states from the database hbtn_0e_0_usa.
Takes 3 arguments: mysql username, mysql password, and database name.
"""

import MySQLdb
import sys


if __name__ == "__main__":
    # Get MySQL credentials from command-line argument
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to MySQL database
    db = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=password,
        db=db_name,
        port=3306
    )
    
    # Create a cursor object to interact with the database
    cursor = db.cursor()
    
    # Execute the SQL query to retrieve states sorted by id
    cursor.execute("SELECT * FROM states ORDER BY id ASC;")
    
    # Fetch all results from the executed query
    rows = cursor.fetchall()
    
    # Print the results as required
    for row in rows:
        print(row)
    
    # Close the cursor and database connection
    cursor.close()
    db.close()
