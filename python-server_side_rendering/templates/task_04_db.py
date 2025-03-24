from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

def get_data_from_json():
    try:
        with open("products.json", "r") as file:
            return json.load(file)
    except Exception as e:
        return {"error": f"Error loading JSON: {str(e)}"}

def get_data_from_csv():
    try:
        with open("products.csv", "r") as file:
            reader = csv.DictReader(file)
            return [row for row in reader]
    except Exception as e:
        return {"error": f"Error loading CSV: {str(e)}"}

def get_data_from_sql():
    try:
        conn = sqlite3.connect("products.db")
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()
        conn.close()

        return [
            {"id": row[0], "name": row[1], "category": row[2], "price": row[3]}
            for row in rows
        ]
    except Exception as e:
        return {"error": f"Error loading SQL data: {str(e)}"}

@app.route('/')
def display_products():
    source = request.args.get('source', 'json')
    if source == 'json':
        data = get_data_from_json()
    elif source == 'csv':
        data = get_data_from_csv()
    elif source == 'sql':
        data = get_data_from_sql()
    else:
        return render_template('product_display.html', products=None, error="Wrong source")

    # Check for error inside the returned data
    if isinstance(data, dict) and "error" in data:
        return render_template('product_display.html', products=None, error=data["error"])

    return render_template('product_display.html', products=data, error=None)

if __name__ == "__main__":
    app.run(debug=True)