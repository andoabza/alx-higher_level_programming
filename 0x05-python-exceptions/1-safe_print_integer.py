#!/usr/bin/python3
def safe_print_integer(value):
    try:
            return int(value)
    except:
        return False
