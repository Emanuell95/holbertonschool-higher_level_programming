#!/usr/bin/python3
class BaseGeometry:
    """
    A class representing a base geometry.
    The class provides a method to calculate the area of a shape.
    If the area is not implemented for a specific shape, an exception is raised.
    """
    def area(self):
        """
        Calculates the area of a given shape.

        Raises:
            Exception: area() is not implemented for this shape
        """
        raise Exception("area() is not implemented")