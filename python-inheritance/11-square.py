#!/usr/bin/python3
"""
This module defines a simple geometry hierarchy with three classes:

- BaseGeometry: A base class with methods for validating integers and computing area (not implemented).
- Rectangle: A subclass of BaseGeometry representing a rectangle with width and height.
- Square: A subclass of Rectangle representing a square with equal sides.
"""

class BaseGeometry:
    """
    A base class for geometry objects.
    """
    
    def area(self):
        """
        Calculates the area of a given shape.

        Raises:
            Exception: area() is not implemented for this shape.
        """
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """
        Validates that a value is a positive integer.
        
        Args:
            name (str): The name of the variable being validated.
            value (int): The value to validate.
        
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is not greater than 0.
        """
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

class Rectangle(BaseGeometry):
    """
    A class representing a rectangle, inheriting from BaseGeometry.
    """
    
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

    def area(self) -> int:
        """
        Calculates the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self) -> str:
        """
        Returns a string representation of the rectangle.

        Returns:
            str: A string in the format [Rectangle] <width>/<height>
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
        
class Square(Rectangle):
    """
    A class representing a square, inheriting from Rectangle.
    """
    
    def __init__(self, size: int):
        """
        Initializes a Square with validated size.

        Args:
            size (int): The size of the square's sides, must be a positive integer.
        
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is not greater than 0.
        """
        self.integer_validator("size", size)  
        self.__size = size  
        super().__init__(size, size)  

    def area(self) -> int:
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def __str__(self) -> str:
        """
        Returns a string representation of the square.

        Returns:
            str: A string in the format [Square] <size>/<size>
        """
        return f"[Square] {self.__size}/{self.__size}"
