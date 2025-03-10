#!/usr/bin/env python3
"""Converts a CSV file to a JSON file."""
import csv
import json

def convert_csv_to_json(csv_filename):
    """Converts a CSV file to a JSON file named data.json."""
    try:
        with open(csv_filename, 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            data = [row for row in reader]
        
        with open('data.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)
        
        return True
    except FileNotFoundError:
        print(f"Error: The file '{csv_filename}' was not found.")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

