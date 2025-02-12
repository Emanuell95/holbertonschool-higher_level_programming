#!/usr/bin/python3

def read_file(filename=""):
    """
    Reads a UTF-8 encoded text file and prints its content to standard output.

    Parameters:
    filename (str): The name of the file to read. Defaults to an empty string.

    Behavior:
    - Opens the specified file in read mode with UTF-8 encoding.
    - Reads and prints the file content to the console.
    - Uses `end=""` in `print()` to avoid adding an extra newline.
    - Assumes the file exists and is readable; does not handle exceptions.
    
    Example usage:
    >>> read_file("example.txt")
    """
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end="")

