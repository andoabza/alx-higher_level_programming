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











