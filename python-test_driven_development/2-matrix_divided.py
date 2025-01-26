#!/usr/bin/python3
def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number.

    Args:
        matrix (list of lists of int/float): The matrix to be divided.
        div (int/float): The divisor.

    Returns:
        list of lists of float: A new matrix with each element divided by div.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats.
                   If rows of the matrix are not of the same size.
                   If div is not a number.
        ZeroDivisionError: If div is 0.
    """
    # Check if matrix is a list of lists containing integers or floats
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(all(isinstance(element, (int, float)) for element in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    # Check if all rows in the matrix are of the same size
    row_length = len(matrix[0]) if matrix else 0
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    
    # Check if div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    
    # Check if div is zero
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    # Divide all elements of the matrix by div, rounded to 2 decimal places
    return [[round(element / div, 2) for element in row] for row in matrix]
