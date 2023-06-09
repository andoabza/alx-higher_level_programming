#!/usr/bin/python3
""" Define REctangle class. """
class Rectangle:
    """ functions:
            width for the width.
            height for the height.
            area for the area.
            perimeter for the perimeter.

        Args:
            width to calculate rectangle.
            height for the rectangle
            value: to set and retrive.
            str to print the str form
            repr to print object
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
    def area(self):
        area = self.__width * self.__height
        return area

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            peri = 2 * (self.__width + self.__height)
            return peri
    
    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        rect = []
        for i in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))
    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"
    def __del__(self):
        del self
        print("Bye rectangle...")
