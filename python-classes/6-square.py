#!/usr/bin/python3
"""Module that defines a Square class with size and position validation, property methods, and additional functionality."""

class Square:
    """Class that defines a square with size and position validation, property methods, area calculation, and printing capability."""
    
    def __init__(self, size=0, position=(0, 0)):
        """Initializes the square with private size and position attributes.
        
        Args:
            size (int): The size of the square. Must be an integer and >= 0.
            position (tuple): The position of the square, must be a tuple of 2 positive integers.
        
        Raises:
            TypeError: If size is not an integer or position is not a tuple of 2 positive integers.
            ValueError: If size is less than 0.
        """
        self.size = size
        self.position = position
    
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
    
    @property
    def position(self):
        """Retrieves the position of the square."""
        return self.__position
    
    @position.setter
    def position(self, value):
        """Sets the position of the square with validation.
        
        Args:
            value (tuple): The new position of the square.
        
        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) and num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
    
    def area(self):
        """Calculates and returns the area of the square.
        
        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
    
    def my_print(self):
        """Prints the square with the character # to stdout.
        If size is 0, prints an empty line.
        Position is considered when printing the square.
        """
        if self.__size == 0:
            print()
            return
        
        for _ in range(self.__position[1]):
            print()
        
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
