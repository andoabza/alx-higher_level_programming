#!/usr/bin/python3
def max_integer(my_list=[]):
    newlist = []
    
    if not my_list:
        newlist = 0, "None"
    else:
        newlist = my_list.sort(reverse=True)
        return my_list[0]
