#!/usr/bin/python3
def safe_print_integer(value):
        if value == int(value):
            try:
                print("{:d}".format(value))
                return True
        except:
            return False
