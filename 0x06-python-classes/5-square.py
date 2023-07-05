#!/usr/bin/python3
""" define square class"""
class Square:
    """func:
            define init tosize.
            define size with getter.
            define size to setter of size.
            define area with return size ** 2.
    Args:
        int (size) for the input"""
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    
    def area(self):
        return self.__size * self.__size
    def my_print(self):
        if self.__size == 0:
            print('')
        else:
            for x in range(0, self.__size):
                print(self.__size * '#', end="\n")

