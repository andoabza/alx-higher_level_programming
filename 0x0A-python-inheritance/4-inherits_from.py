#!/usr/bin/python3
def inherits_from(a_class, obj):
    if isinstance(obj, type(a_class)) and issubclass(type(obj), a_class):
        return False
    return True
