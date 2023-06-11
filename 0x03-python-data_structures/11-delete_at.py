#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    new = []
    if idx < 0 or idx > len(my_list):
        new = my_list
        return my_list
    else:
        new =  my_list.remove(idx + 1)
        return my_list
