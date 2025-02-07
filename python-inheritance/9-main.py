#!/usr/bin/python3
"""
This module demonstrates the usage of the Rectangle class.
It creates a Rectangle object and prints its area.
"""

Rectangle = __import__('9-rectangle').Rectangle

"""
Import the Rectangle class from the module 9-rectangle.py.

The Rectangle class is expected to be defined in 9-rectangle.py,
which provides methods for geometric calculations, including area computation.
"""

r = Rectangle(3, 5)

print(r)
print(r.area())
