#!/usr/bin/python3
class Square:
    """ define square class that raise exception if false"""
    def __init__(self, size=0):
        """ self private attribute
        Args: 
            int(size): to raise  exception.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
