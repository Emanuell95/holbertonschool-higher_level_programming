#!/usr/bin/python3
""" 
This module provides a function to check if an object is an instance of a specified class 
or if it is an instance of a class that inherited from the specified class.

Functions:
    inherits_from(obj, a_class): 
        Determines whether an object is an instance of a class or an instance of a subclass of that class.
"""
def inherits_from(obj, a_class):
    """
    Checks if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class.

    Args:
        obj (object): The object to check.
        a_class (class): The class to check against.

    Returns:
        bool: True if obj is an instance of a_class, False otherwise.
    """
    return type(obj) == a_class