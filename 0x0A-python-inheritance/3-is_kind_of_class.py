#!/usr/bin/python3
""" define a function that return class name. """
def is_kind_of_class(obj, a_class):
    """ return name if True otherwise False. """
    if isinstance(obj, a_class):
        return True
    return False
