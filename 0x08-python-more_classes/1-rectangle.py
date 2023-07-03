#!/usr/bin/python3
""" Define REctangle class. """
class Rectangle:
    """ functions:
            width for the width.
            height for the height.
        Args:
            value: to set and retrive.
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
   
    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value






























