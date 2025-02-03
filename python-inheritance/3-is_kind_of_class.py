#!/usr/bin/python3
def is_kind_of_class(obj, a_class):
    """
    Checks if the object is an instance of, or if the object is an instance of a class that
    inherited from, the specified class.

    Args:
        obj (object): The object to check.
        a_class (class): The class to check against.

    Returns:
        bool: True if obj is an instance of a_class, False otherwise.
    """
    return isinstance(obj, a_class)