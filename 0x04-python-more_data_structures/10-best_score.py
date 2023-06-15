#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == None:
        maxval = None
        return maxval
    else:
        maxval = max(a_dictionary, key=a_dictionary.get)
        return  maxval















