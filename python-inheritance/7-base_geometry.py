#!/usr/bin/python3
"""
This module defines a base class for geometric operations.
It provides a method to calculate the area of a geometric shape and a method to validate if a given value is a positive integer.
If the method is not yet implemented, it raises an exception."""
class BaseGeometry:
    """
    Calculates the area of a given shape.

    Raises:
        Exception: area() is not implemented for this shape
    """
    def area(self):
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")