#!/usr/bin/env python3
"""Basic serialization of a Python dictionary to a JSON file."""
import json

def serialize_and_save_to_file(data, filename):
    """Serializes a Python dictionary to a JSON file."""
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

def load_and_deserialize(filename):
    """Loads a JSON file and returns the deserialized Python dictionary."""
    with open(filename, 'r') as file:
        return json.load(file)


