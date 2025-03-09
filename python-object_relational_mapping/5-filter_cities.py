#!/usr/bin/python3
"""
Lists all cities of a given state from the database hbtn_0e_4_usa,
ensuring safety from SQL injection.
Takes 4 arguments: mysql username, mysql password, database name, and state name.
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
        
        # Execute the SQL query safely using a parameterized query
        query = ("SELECT cities.id, cities.name FROM cities "
                 "JOIN states ON cities.state_id = states.id "
                 "WHERE states.name = %s ORDER BY cities.id ASC;")
        cursor.execute(query, (state_name,))
        
        # Fetch all results from the executed query
        rows = cursor.fetchall()
        
        # Print the results in the required format
        print(", ".join(row[1] for row in rows))
        
    except MySQLdb.Error as e:
        print(f"Error: {e}")
    
    finally:
        # Close the cursor and database connection
        if 'cursor' in locals():
            cursor.close()
        if 'db' in locals():
            db.close()
