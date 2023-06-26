#!/usr/bin/python3
def safe_print_integer(value):
    try:
        if value == int(value):
            print(value)
            return True
    except:
        return False
