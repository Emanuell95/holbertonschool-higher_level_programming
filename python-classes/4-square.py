#!/usr/bin/python3
"""Module that defines a Square class with size validation, a property, and an area method."""

class Square:
    """Class that defines a square with size validation, property methods, and an area method."""
    
    def __init__(self, size=0):
        """Initializes the square with a private size attribute.
        
        Args:
            size (int): The size of the square. Must be an integer and >= 0.
        
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.size = size
    
    @property
    def size(self):
        """Retrieves the size of the square."""
        return self.__size
    
    @size.setter
    def size(self, value):
        """Sets the size of the square with validation.
        
        Args:
            value (int): The new size of the square.
        
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    
    def area(self):
        """Calculates and returns the area of the square.
        
        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
