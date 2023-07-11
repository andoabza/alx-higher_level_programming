#!/usr/bin/python3
""" import a class.to 11-square.py """
Rectangle = __import__('9-rectangle').Rectangle
""" define a class. """
class Square(Rectangle):
    """ intializing size:
    to compute square
    """
    def __init__(self, size):
        super().integer_validator("size", size)
        self.__size = size
    def area(self):
        """ return square """
        return self.__size ** 2
    def __str__(self):
        """ write the output. """
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__size) + "/" + str(self.__size)
        return string

