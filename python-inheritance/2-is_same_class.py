#!/usr/bin/python3
"""
Module: is_same_class

This module defines a function `is_same_class` that checks whether
a given object is exactly an instance of a specified class.

Functions:
    - is_same_class(obj, a_class): Returns True if `obj` is an exact instance 
      of `a_class`, otherwise returns False.

Example Usage:
    >>> is_same_class(5, int)
    True
    >>> is_same_class(5, float)
    False
    >>> is_same_class("hello", str)
    True
    >>> is_same_class([1, 2, 3], list)
    True
    >>> is_same_class(True, int)  # `bool` is a subclass of `int`
    False
"""
def is_same_class(obj, a_class):
    """
    Returns True if the object is exactly an instance of the specified class; otherwise False.

    Args:
        obj (object): The object to check.
        a_class (class): The class to check against.

    Returns:
        bool: True if obj is an instance of a_class, False otherwise.
    """
    return type(obj) == a_class