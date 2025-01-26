#!/usr/bin/python3
"""
The ``3-say_my_name`` module

This module provides the ``say_my_name`` function, which prints
a formatted name.

Usage:

    Import the function:

        >>> say_my_name = __import__('3-say_my_name').say_my_name

    Now test it:

        >>> say_my_name("John", "Smith")
        My name is John Smith

        >>> say_my_name("Bob")
        My name is Bob

        >>> say_my_name(12, "White")
        Traceback (most recent call last):
        TypeError: first_name must be a string

        >>> say_my_name("Barry", None)
        Traceback (most recent call last):
        TypeError: last_name must be a string

        >>> say_my_name(1, 2)
        Traceback (most recent call last):
        TypeError: first_name must be a string

        >>> say_my_name("", "Holberton")
        My name is  Holberton

        >>> say_my_name("", "")
        My name is

        >>> say_my_name()
        Traceback (most recent call last):
        TypeError: say_my_name() missing 1 required positional argument: 'first_name'
"""

def say_my_name(first_name, last_name=""):
    """
    Prints "My name is <first_name> <last_name>".

    Args:
        first_name (str): The first name.
        last_name (str): The last name. Default is an empty string.

    Raises:
        TypeError: If first_name or last_name is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    
    print(f"My name is {first_name} {last_name}")
