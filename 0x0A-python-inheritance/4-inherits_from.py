#!/usr/bin/python3
""" define a function that inhert. """
def inherits_from(a_class, obj):
    """ return TRue and False. """
    if isinstance(obj, type(a_class)) and issubclass(type(obj), a_class):
        return False
    return True
