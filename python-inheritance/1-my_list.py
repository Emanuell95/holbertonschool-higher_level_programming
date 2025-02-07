#!/usr/bin/python3
"""
Module: 1-my_list
This module defines a class `MyList` that inherits from the built-in `list` class.
It includes a method to print the list in sorted order without modifying the original list.
"""

class MyList(list):
    """
    A subclass of the built-in `list` class with an additional method.
    """
    
    def print_sorted(self):
        """
        Prints a sorted version of the list without modifying the original list.
        
        The method sorts the elements of the list in ascending order and prints them,
        but does not alter the list itself.
        """
        sorted_list = sorted(self)  # Sort the list without changing the original
        print(sorted_list)
