#!/usr/bin/python3
""" import  class. """
Rectangle = __import__('9-rectangle').Rectangle
""" define class. """
class Square(Rectangle):
    """Initialize a new square.

        Args:
            size (int): The size of the new square.
    """
    def __init__(self, size):
        """ define every thing. """
        super().integer_validator("size", size)
        super().__init__(size, size)  
        self.__size = size
