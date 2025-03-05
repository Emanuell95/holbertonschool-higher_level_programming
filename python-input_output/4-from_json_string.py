#!/usr/bin/python3
"""
Module that provides a function to convert a JSON string to an object."""
import json
def from_json_string(my_str):
    """
    Returns the JSON representation of the given string.

    Parameters:
    my_str (str): String to be converted to a JSON object.

    Returns:
    object: JSON object representation of the given string.
    """
    
    return json.loads(my_str)