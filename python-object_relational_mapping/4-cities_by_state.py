#!/usr/bin/python3
"""
Lists all cities from the database hbtn_0e_4_usa.
Takes 3 arguments: mysql username, mysql password, and database name.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./script.py <username> <password> <database>")
        sys.exit(1)

    # Get MySQL credentials from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

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
        
        # Execute the SQL query to retrieve all cities sorted by id
        cursor.execute("SELECT * FROM cities ORDER BY id ASC;")
        
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