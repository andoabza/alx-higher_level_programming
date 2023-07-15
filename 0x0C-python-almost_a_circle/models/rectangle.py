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
    def update(self, *args, **kwargs):
        """ update the args with kwargs. """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v
    """ dict representation """
    def to_dictionary(self):
        return {
                'x' : self.x,
                'y' : self.y,
                'id' : self.id,
                'width' : self.width,
                'height' : self.height
                }




