import requests

url = "http://127.0.0.1:5000/add_user"
headers = {"Content-Type": "application/json"}
data = {
    "username": "alice",
    "name": "Alice",
    "age": 25,
    "city": "San Francisco"
}

response = requests.post(url, json=data, headers=headers)

print("Status Code:", response.status_code)
try:
    print("Response:", response.json())
except requests.exceptions.JSONDecodeError:
    print("Response content:", response.text)  # Prints raw response if not JSON