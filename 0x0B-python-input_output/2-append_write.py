#!/usr/bin/python3
""" append_write a function that open file in append mode. """
def append_write(filename="", text=""):
    """ open file as appending then text is inserted into the file. """
    with open(filename, 'a') as f:
        return f.write(text)
    
