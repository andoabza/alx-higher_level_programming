#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newlist = []
    for i in range(len(matrix)):
        newlist =  [j * j for j in range(len(matrix[i]))]
        def sqare(j):
            return x*x
        newlist = map(sqare, matrix)
        return matrix 
