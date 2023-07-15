#!/usr/bin/python3
""" import Rectangle """
from models.rectangle import Rectangle
""" square class that inhert from Rectangle. """
class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square.

            Args:
            size (int): The size of the new Square.
            x (int): The x coordinate of the new Square.
            y (int): The y coordinate of the new Square.
            id (int): The identity of the new Square.
        """
        super().__init__(size, size, x, y, id)
    
    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    """ string representation. """
    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)
    def update(self, *args, **kwargs):
        """ update the args with kwargs. """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.width = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    """ dict representation. """
    def to_dictionary(self):
        return {
                'id' : self.id,
                'x' : self.x,
                'size' : self.width,
                'y' : self.y
                }








