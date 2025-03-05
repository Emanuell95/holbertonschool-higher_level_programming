#!/usr/bin/python3
""" 
This module provides a function to check if an object is an instance of a specified class 
or if it is an instance of a class that inherited from the specified class.

Functions:
    is_kind_of_class(obj, a_class): 
        Determines whether an object is an instance of a class or an instance of a subclass of that class.
"""

def is_kind_of_class(obj, a_class):
    """
    Checks if the object is an instance of, or if the object is an instance of a class that
    inherited from, the specified class.

    Args:
        obj (object): The object to check.
        a_class (class): The class to check against.

    Returns:
        bool: True if obj is an instance of a_class or a subclass, False otherwise.
    """
    return isinstance(obj, a_class)
