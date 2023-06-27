#!/usr/bin/python3
""" Define a clss """
class Square:
    """ define a init for the self
    Args:
        int(size) for the area and clac"""
    def __init__(self, size=0):
        if size is not int(size):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        
        self.__size = size
        """ define func that return area"""
    def area(self):
        return self.__size * self.__size
        
