from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', title='Welcome')

@app.route('/items')
def items():
    # Read data from the JSON file
    try:
        with open('items.json', 'r') as file:
            data = json.load(file)
            items_list = data.get('items', [])
    except (FileNotFoundError, json.JSONDecodeError):
        # Handle errors: file not found or invalid JSON
        items_list = []
    
    # Render the template with the items list
    return render_template('items.html', title='Items List', items=items_list)

if __name__ == '__main__':
    app.run(debug=True)