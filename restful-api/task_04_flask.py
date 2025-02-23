from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}

@app.route('/')
def home():
    return "Welcome to the Flask API!"

@app.route('/data')
def get_data():
    return jsonify(sorted(list(users.keys())))  # Ensure a consistent order

@app.route('/status')
def status():
    return "OK"

@app.route('/users/<username>')
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()

    # Check if JSON data is valid and contains "username"
    if not data or "username" not in data:
        return jsonify({"error": "Username is required"}), 400
    
    username = data["username"].strip().lower()  # Ensure consistent username storage (case-insensitive)

    # Check for duplicate username
    if username in users:
        return jsonify({"error": "User already exists"}), 400

    # Store user data with lowercase username to prevent case-sensitive duplicates
    users[username] = {
        "username": username,  # Ensure username is stored properly
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }

    return jsonify({"message": "User added", "user": users[username]}), 201

if __name__ == "__main__":
    app.run(debug=True)