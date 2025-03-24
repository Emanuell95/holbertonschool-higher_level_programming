# task_03_files.py
from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

def read_json_data(file_path="products.json"):
    """Read and parse data from a JSON file."""
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return None
    except json.JSONDecodeError:
        return None

def read_csv_data(file_path="products.csv"):
    """Read and parse data from a CSV file."""
    try:
        products = []
        with open(file_path, 'r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                # Convert id to int and price to float for consistency
                row['id'] = int(row['id'])
                row['price'] = float(row['price'])
                products.append(row)
        return products
    except FileNotFoundError:
        return None

@app.route('/products')
def display_products():
    # Get query parameters
    source = request.args.get('source', '')
    product_id = request.args.get('id')
    
    # Initialize variables
    products = []
    error_message = None
    
    # Determine the data source and read the appropriate file
    if source == 'json':
        products = read_json_data()
    elif source == 'csv':
        products = read_csv_data()
    else:
        error_message = "Wrong source"
    
    # Filter by ID if provided
    if product_id and not error_message and products:
        try:
            product_id = int(product_id)
            filtered_products = [p for p in products if p['id'] == product_id]
            if filtered_products:
                products = filtered_products
            else:
                error_message = "Product not found"
        except ValueError:
            error_message = "Invalid ID format"
    
    # Render the template with the data
    return render_template('product_display.html', 
                          products=products, 
                          error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True)