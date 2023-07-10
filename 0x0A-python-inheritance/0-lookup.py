#!/usr/bin/python3
""" define a function that return methods of obj. """
def lookup(obj):
    """ look for list of methods lookup(obj) or class."""
    obj1 = dir(obj)
    return (obj1)
