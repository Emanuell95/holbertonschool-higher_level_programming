#!/usr/bin/python3
import http.server
import json
from http import HTTPStatus

class SimpleHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        """
        Handles a GET request to the server.
        
        The server responds to the following endpoints:
        
        * / : A simple text response with a "Hello, this is a simple API!" message.
        * /data : Returns a JSON object containing some sample data.
        * /status : Returns a JSON object with a "status" key and a value of "OK".
        * /info : Returns a JSON object with some information about the API.
        * All other endpoints : Returns a JSON object with a 404 error message.
        """
        
        if self.path == '/':
            self.send_response(HTTPStatus.OK)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
        
        elif self.path == '/data':
            data = {"name": "John", "age": 30, "city": "New York"}
            self.send_response(HTTPStatus.OK)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(data).encode('utf-8'))
        
        elif self.path == '/status':
            self.send_response(HTTPStatus.OK)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"status": "OK"}).encode('utf-8'))
        
        elif self.path == '/info':
            info = {"version": "1.0", "description": "A simple API built with http.server"}
            self.send_response(HTTPStatus.OK)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(info).encode('utf-8'))
        
        else:
            self.send_response(HTTPStatus.NOT_FOUND)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"error": "Endpoint not found"}).encode('utf-8'))

if __name__ == "__main__":
    PORT = 8000
    server_address = ("", PORT)
    httpd = http.server.HTTPServer(server_address, SimpleHTTPRequestHandler)
    print(f"Serving on port {PORT}...")
    httpd.serve_forever()
