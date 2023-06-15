#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    new = list(a_dictionary)
    if str(key) in new:
        new.pop(key)
        new.append(value)
    else:
        new.append(value)
    return new






















