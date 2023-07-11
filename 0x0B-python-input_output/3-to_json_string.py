#!/usr/bin/python3
import json
def to_json_string(my_obj):
    return (json.dumps(my_obj, sort_keys = True))
    try:
        json.dumps(my_obj)
        return True
    except (TypeError, OverflowError):
        return False

















