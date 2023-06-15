#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    new = str(key)
    if new in a_dictionary:
        a_dictionary.pop(new)
        a_dictionary.update({new: value})
        return a_dictionary
    else:
        a_dictionary.update({new: value})
        return a_dictionary






















