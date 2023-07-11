#!/usr/bin/python3
""" import json. """
import json
""" define a function that save to file. """
def save_to_json_file(my_obj, filename):
    """ save to file with write mode. """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
