#!/usr/bin/python3
""" import the module """
from models.base import Base
""" define a class. """
class Rectangle(Base):

    """
    write a class that inhert fromn `Base` and a class of the folloeing args with private attribiute of width, height, x, y with getter setter.
    Args: width, height, x, y
    value to manage the exceptions.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
    
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)
    
    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
    
    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value
    
    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value
    
    @property
    def y(self):
        return self.__y
    
    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
    
    """ define area to calculate area. """
    def area(self):
        return self.__width * self.__height
    
    """ define display to print #"""
    def display(self):
         for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")
    
    """ define __str__ to print out string representation. """
    def __str__(self):
        return f"{self.__class__.__name__} ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}"

    """ define update for args. """
    def update(self, *args):
        if len(args) == 1:
            self.id = args[0]
        elif len(args) == 2:
            self.id = args[0]
            self.__width = args[1]
        elif len(args) == 3:
            self.id = args[0]
            self.__width = args[1]
            self.__height = args[2]
        elif len(args) ==  4:
            self.__width = args[1]
            self.__height = args[2]
            self.__x = args[3]
        elif len(args) ==  5:
            self.id = args[0]
            self.__width = args[1]
            self.__height = args[2]
            self.__x = args[3]
            self.__y = args[4]















