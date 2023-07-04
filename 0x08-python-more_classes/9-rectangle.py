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
    number_of_instances = 0
    print_symbol = '#'
    def __init__(self, width=0, height=0):
        type(self).number_of_instances += 1
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
        stri = ""
        for i in range(self.height):
            for j in range(self.width):
                stri += str(self.print_symbol)
            if i == self.height - 1:
                break
            else:
                stri += "\n"
        return stri
    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"
    def __del__(self):  
        
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        elif rect_1.area() == rect_2.area():
            return rect_1
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
    @classmethod
    def square(cls, size=0):
        return cls(size, size)
