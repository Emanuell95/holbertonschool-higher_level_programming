#!/usr/bin/python3
"""Module that defines a Square class with a private size attribute."""

class Square:
    """Class that defines a square with size validation and an area method."""
    
    def __init__(self, size=0):
        """Initializes the square with a private size attribute.
        
        Args:
            size (int): The size of the square. Must be an integer and >= 0.
        
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    
    def area(self):
        """Calculates and returns the area of the square.
        
        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
