#!/usr/bin/python3
def matrix_divided(matrix, div):
    """ define a dividing function. 
    check if list is int or float.
    check if they have the same size.
    check if div is a number.
    check if div isn't 0.
    return the numer and round to 2.
    """
    
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
    
            if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
                    raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        
            row_size = len(matrix[0])
            if not all(len(row) == row_size for row in matrix):
                raise TypeError("Each row of the matrix must have the same size")
            
            if not isinstance(div, (int, float)):
                raise TypeError("div must be a number")
            
            if div == 0:
                raise ZeroDivisionError("division by zero")
            
            result = [[round(row/div, 2) for row in list]for list in matrix]
            return result
