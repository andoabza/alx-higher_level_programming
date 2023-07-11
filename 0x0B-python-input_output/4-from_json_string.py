#!/usr/bin/python3
""" import the json> """
import json
""" define a function that decode."""
def from_json_string(my_str):
    """ return to string from json object."""
    new = json.JSONDecoder().decode(my_str)
    return (new)







