from flask import Flask, render_template, request
import json
import csv
import sqlite3
import os

app = Flask(__name__)

# Function to read data from JSON file
def read_json_data():
    try:
        with open('products.json', 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error reading JSON file: {e}")
        return None

# Function to read data from CSV file
def read_csv_data():
    try:
        products = []
        with open('products.csv', 'r') as f:
            csv_reader = csv.DictReader(f)
            for row in csv_reader:
                products.append(row)
        return products
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return None

# Function to read data from SQLite database
def read_sqlite_data():
    try:
        conn = sqlite3.connect('products.db')
        # Set row_factory to get dictionary-like objects
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Products')
        rows = cursor.fetchall()
        
        # Convert rows to dictionaries
        products = []
        for row in rows:
            products.append({key: row[key] for key in row.keys()})
        
        conn.close()
        return products
    except Exception as e:
        print(f"Error reading SQLite database: {e}")
        return None

# Function to create and populate the database if it doesn't exist
def setup_database():
    if not os.path.exists('products.db'):
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Products (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                category TEXT NOT NULL,
                price REAL NOT NULL
            )
        ''')
        cursor.execute('''
            INSERT INTO Products (id, name, category, price)
            VALUES
            (1, 'Laptop', 'Electronics', 799.99),
            (2, 'Coffee Mug', 'Home Goods', 15.99)
        ''')
        conn.commit()
        conn.close()
        print("Database created and populated successfully")

# Set up the database when the application starts
setup_database()

@app.route('/')
def index():
    source = request.args.get('source', default='json')
    
    if source == 'json':
        data = read_json_data()
        if data is None:
            return "Error reading JSON data", 500
    elif source == 'csv':
        data = read_csv_data()
        if data is None:
            return "Error reading CSV data", 500
    elif source == 'sql':
        data = read_sqlite_data()
        if data is None:
            return "Error reading SQLite data", 500
    else:
        return "Wrong source", 400
    
    return render_template('product_display.html', products=data)

if __name__ == '__main__':
    app.run(debug=True)