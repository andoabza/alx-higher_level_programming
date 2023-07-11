#!/usr/bin/python3
""" import json. """
import json
""" define  load_from_json_file for save."""
def load_from_json_file(filename):
    """ oen file in read mode. """
    with open(filename, 'r') as f:
        return json.dumps(filename)
















