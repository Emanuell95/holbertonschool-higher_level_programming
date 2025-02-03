#!/usr/bin/python3
class BaseGeometry:
    def area(self):
        """
        Calculates the area of a given shape.

        Raises:
            Exception: area() is not implemented for this shape
        """
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

class Rectangle(BaseGeometry):
    def __init__(self, width: int, height: int):
        """
        Initializes a Rectangle with validated width and height.

        Args:
            width (int): The width of the rectangle, must be a positive integer.
            height (int): The height of the rectangle, must be a positive integer.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is not greater than 0.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
        
        

