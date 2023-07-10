#!/usr/bin/python3
""" define a func that check if a class and return the class na,e. """ 
def is_same_class(obj, a_class):
    """ that return True if is class of a_class else False. """
    if type(obj) == a_class:
        return True
    return False
