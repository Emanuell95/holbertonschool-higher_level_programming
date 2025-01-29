#!/usr/bin/python3
class Square:
    """Defines a square with size validation and area calculation."""
    
    def __init__(self, size=0):
        """Initializes a square with a given size."""
        self.size = size  # Using the property setter for validation
    
    @property
    def size(self):
        """Retrieves the size of the square."""
        return self.__size
    
    @size.setter
    def size(self, value):
        """Sets the size of the square with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    
    def area(self):
        """Returns the area of the square."""
        return self.__size ** 2

