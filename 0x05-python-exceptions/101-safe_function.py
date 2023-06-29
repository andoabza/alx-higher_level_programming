#!/usr/bin/python3
import sys
def safe_function(fct, *args):
    try:
        return fct(*args)
    except IndexError as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
    except:
        pass
