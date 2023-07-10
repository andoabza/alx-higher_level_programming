#!/usr/bin/python3
""" define a MyList class. """
class MyList(list):
    """ return sorted list. """
    def print_sorted(self):
        print(sorted(self))
