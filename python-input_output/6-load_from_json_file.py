#!/usr/bin/python3
"""Module that provides a function to load an object from a JSON file."""
import json

def load_from_json_file(filename):
    """
    Loads an object from a given JSON file.

    Parameters:
    filename (str): The name of the JSON file to read from.

    Returns:
    object: The object read from the JSON file.

    Raises:
    FileNotFoundError: If the given filename does not exist.
    """
    with open(filename, 'r') as file:
        return json.load(file)
