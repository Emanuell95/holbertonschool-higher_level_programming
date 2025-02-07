#!/usr/bin/python3
"""
This module demonstrates the usage of the Rectangle class.
It creates a Rectangle object and prints its area
"""
Rectangle = __import__('9-rectangle').Rectangle

r = Rectangle(3, 5)

print(r)
print(r.area())