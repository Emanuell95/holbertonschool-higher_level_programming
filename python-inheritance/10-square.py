#!/usr/bin/python3
""" This module defines a class Rectangle """
"""
This module defines geometric classes: BaseGeometry, Rectangle, and Square.

Classes:
    BaseGeometry: A base class for geometric operations.
    Rectangle: A subclass of BaseGeometry that represents a rectangle.
    Square: A subclass of Rectangle that represents a square.
"""

class BaseGeometry:
    """
    A base class for geometry-related operations.
    
    Methods:
        area(): Raises an exception as it is not implemented.
        integer_validator(name, value): Validates that value is a positive integer.
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
        Validates if a given value is a positive integer.

        Args:
            name (str): The name of the parameter.
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
    A class that represents a rectangle, inheriting from BaseGeometry.
    
    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.
    
    Methods:
        area(): Returns the area of the rectangle.
        __str__(): Returns a string representation of the rectangle.
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
    A class that represents a square, inheriting from Rectangle.
    
    Attributes:
        __size (int): The size of the square.
    
    Methods:
        area(): Returns the area of the square.
        __str__(): Returns a string representation of the square.
    """
    
    def __init__(self, size: int):
        """
        Initializes a Square with a validated size.

        Args:
            size (int): The size of the square, must be a positive integer.

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
        return f"[Rectangle] {self.__size}/{self.__size}"
