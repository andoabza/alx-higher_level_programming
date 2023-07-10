#!/usr/bin/python3
""" define a class that return """
class BaseGeometry:
    """ area a func that raise exception. """
    def area(self):
        raise Exception("area() is not implemented")
    """ func that return namme"""
    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
