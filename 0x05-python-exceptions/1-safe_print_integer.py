#!/usr/bin/python3
def safe_print_integer(value):
    try:
        if value == int(value):
            return value
    except:
        return value
