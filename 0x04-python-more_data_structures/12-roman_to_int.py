#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    value = 0
    
    for i in range(len(roman_string)-1, -1, -1):
        now = roman[roman_string[i]]
        if now < value:
            result -= now
        else:
            result += now
            value = now
    
    return result



















