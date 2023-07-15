#!/usr/bin/python3
""" import json """
import json
""" define a class. """
class Base:
    """ define a class that assing a value to id
    Args:
    __nb_objects : a value to be assigned when args is not given
    id : the var yto be assigned.
    """
    __nb_objects = 0
    def __init__(self, id=None):
        self.id = id
        if self.id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
    """ json string """
    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
