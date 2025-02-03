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