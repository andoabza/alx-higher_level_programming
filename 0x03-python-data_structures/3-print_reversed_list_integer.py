#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for items in reversed(my_list):
        print("{:n}".format(items))
        items = items+1
