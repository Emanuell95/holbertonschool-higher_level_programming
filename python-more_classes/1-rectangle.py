#!/usr/bin/python3
class Rectangle:
    """
<<<<<<< HEAD
    A class that defines a rectangle.
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
=======
    A class used to represent a Rectangle.

    Attributes:
    -----------
    width : int
        The width of the rectangle (must be an integer >= 0)
    height : int
        The height of the rectangle (must be an integer >= 0)
    """
    
    def __init__(self, width=0, height=0):
        """Initializes the rectangle with optional width and height."""
        self.width = width
        self.height = height
    
    @property
    def width(self):
        """Gets the width of the rectangle."""
        return self.__width
    
    @width.setter
    def width(self, value):
        """Sets the width of the rectangle, ensuring it is a non-negative integer."""
>>>>>>> 524550f753e0cae514ef13d2489a5c00a12f8bc3
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
<<<<<<< HEAD

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
=======
    
    @property
    def height(self):
        """Gets the height of the rectangle."""
        return self.__height
    
    @height.setter
    def height(self, value):
        """Sets the height of the rectangle, ensuring it is a non-negative integer."""
>>>>>>> 524550f753e0cae514ef13d2489a5c00a12f8bc3
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
<<<<<<< HEAD

=======
>>>>>>> 524550f753e0cae514ef13d2489a5c00a12f8bc3
