#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('8-rectangle').Rectangle
"""Represent a rectangle using BaseGeometry."""
class Rectangle(Rectangle, BaseGeometry):
    """Intialize a new Rectangle.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
    """
    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)

        self.__width = width
        self.__height = height
    def area(self):
        """ return area. """
        return self.__width * self.__height
    def __str__(self):
        """ write the output. """
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string

