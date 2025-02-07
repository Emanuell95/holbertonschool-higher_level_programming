#!/usr/bin/python3
class BaseGeometry:
    """
    A class representing a base geometry.
    """
    def area(self):
        """
        Calculates the area of a given shape.

        Raises:
            Exception: area() is not implemented for this shape
        """
        raise Exception("area() is not implemented")