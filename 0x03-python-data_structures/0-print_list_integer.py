#!/usr/bin/python3
def print_list_integer(my_list=[]):
    for items in my_list:
        print("{:d}".format(items))
        items = items+1
my_list = [1, 2, 3, 4, 5]
print_list_integer(my_list)

