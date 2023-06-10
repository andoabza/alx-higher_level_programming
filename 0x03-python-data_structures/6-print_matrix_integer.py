#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
     for i in matrix:
          matrix = ' '.join(map(str, i))
          print("{}".format(matrix))
