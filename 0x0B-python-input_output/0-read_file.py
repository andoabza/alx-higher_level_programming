#!/usr/bin/python3
""" define a function that read file. """
def read_file(filename=""):
    """ open file name."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end='' )
