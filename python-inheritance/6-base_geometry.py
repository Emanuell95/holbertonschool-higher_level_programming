#!/usr/bin/python3
"""
This module provides functions to check the inheritance and instance relationships of objects.

Functions:
    is_kind_of_class(obj, a_class):
        Determines whether an object is an instance of a class or an instance of a subclass of that class.
    inherits_from(obj, a_class):
        Determines whether an object is an instance of a subclass (directly or indirectly) of a specified class,
        but not an instance of the specified class itself.
"""
def is_kind_of_class(obj, a_class):
    """
    Determines if an object is an instance of a class or an instance of a subclass of that class.

    Args:
        obj (object): The object to check.
        a_class (type): The class to check against.

    Returns:
        bool: True if obj is an instance of a_class or a subclass, False otherwise.
    """
    return isinstance(obj, a_class)

def inherits_from(obj, a_class):
    """
    Determines if an object is an instance of a subclass (directly or indirectly) of a specified class,
    but not an instance of the specified class itself.

    Args:
        obj (object): The object to check.
        a_class (type): The class to check against.

    Returns:
        bool: True if obj is an instance of a subclass of a_class, but not a direct instance of a_class.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
