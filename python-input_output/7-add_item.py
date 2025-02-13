#!/usr/bin/python3
"""
Script that adds all arguments to a Python list and saves them to a file.
Inside the script, import the save_to_json_file module and load_from_json_file module.
Use the load_from_json_file function to load the list from the file.
Use the save_to_json_file function to save the updated list to the file."""
import sys
from save_to_json_file import save_to_json_file
import load_from_json_file  # Import the module

filename = "add_item.json"


try:
    items = load_from_json_file.load_from_json_file(filename)  # Use the function with its module name
except FileNotFoundError:
    items = []

# Add all arguments except script name
items.extend(sys.argv[1:])

# Save the updated list to the file
save_to_json_file(items, filename)