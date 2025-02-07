#!/usr/bin/python3
"""
This module provides a function to return the list of available attributes
and methods of an object.
"""

def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Args:
        obj (object): An instance of a class

    Returns:
        list: A list of attributes and methods
    """
    return list(dir(obj))