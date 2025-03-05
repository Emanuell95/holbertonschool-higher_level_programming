#!/usr/bin/python3
"""Module that provides a function to convert an object to a JSON string."""
import json
def to_json_string(my_obj):
    """
    Returns a JSON string representation of the given object.

    Parameters:
    my_obj (object): Object to be converted to a JSON string.

    Returns:
    str: JSON string representation of the given object.
    """
    return json.dumps(my_obj)