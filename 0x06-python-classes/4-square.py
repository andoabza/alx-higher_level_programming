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
        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self._size = value
    
    def area(self):
        return self.size * self.size
