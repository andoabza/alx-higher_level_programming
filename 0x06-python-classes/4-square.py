#!/usr/bin/python3
""" define square class"""
class Square:
    """ def init tosize.
    Args:
        int (size) for the input"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.size = size
        self.__size = size
        def size(self):
            return self.__size
            def size(self, value):
                self.__size = value
    def area(self):
        return self.__size * self.__size
