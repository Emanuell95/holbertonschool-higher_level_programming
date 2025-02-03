#!/usr/bin/python3
def lookup(obj):
    """
    Returns a list of available attributes and methods of an object:

    Args:
        obj (object): An instance of a class

    Returns:
        list: A list of attributes and methods
    """
    return list(dir(obj))