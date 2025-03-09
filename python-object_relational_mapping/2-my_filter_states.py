#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa where name matches the argument.
Takes 4 arguments: mysql username, mysql password, database name, and state name searched.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: ./script.py <username> <password> <database> <state name>")
        sys.exit(1)

    # Get MySQL credentials and state name from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    try:
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
        
        # Execute the SQL query with user input using format
        query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC;".format(state_name)
        cursor.execute(query)
        
        # Fetch all results from the executed query
        rows = cursor.fetchall()
        
        # Print the results as required
        for row in rows:
            print(row)
        
    except MySQLdb.Error as e:
        print(f"Error: {e}")
    
    finally:
        # Close the cursor and database connection
        if 'cursor' in locals():
            cursor.close()
        if 'db' in locals():
            db.close()
