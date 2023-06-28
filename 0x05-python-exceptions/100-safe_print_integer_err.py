#!/usr/bin/python3
import sys
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except ValueError as e:
        def eprint(*args, **kwargs):
            print(*args, file=sys.stderr, **kwargs)
        eprint(e)

