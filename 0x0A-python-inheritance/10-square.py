#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
class Square(Rectangle):
    def __init__(self, size):
        super().integer_validator("size", size)
        self.__size = size
    def area(self):
        return self.__size ** 2
    def __str__(self):
        """ write the output. """
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__size) + "/" + str(self.__size)
        return string
