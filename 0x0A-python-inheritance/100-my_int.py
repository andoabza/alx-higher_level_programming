#!/usr/bin/python3
""" write a class that inhert int, """
class MyInt(int):
    """ the __eq__ method, it calls the parent class's __eq__ method and negates the result, """
    def __eq__(self, other):
        return not super().__eq__(other)

    def __ne__(self, other):
        """ he __ne__ method, it calls the parent class's __ne__ method and negates the result. """
        return not super().__ne__(other)
