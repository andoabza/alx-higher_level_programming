#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        return a / b
    except:
        return None
    finally:
        try:
            print("Inside result: {}".format(a / b))
        except:
            print("Inside result: {}".format(None))
