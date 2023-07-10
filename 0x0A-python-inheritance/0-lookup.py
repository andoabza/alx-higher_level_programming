#!/usr/bin/python3
def lookup(obj):
    """ look for list of methods lookup(obj) or class."""
    obj1 = dir(obj)
    return list(obj1)
