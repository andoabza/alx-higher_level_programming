#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            element_1 = my_list_1[i]
            element_2 = my_list_2[i]
            if isinstance(element_1, (int, float)) or isinstance(element_2, (int, float)):
                result.append(element_1 / element_2)
        except IndexError:
            print("out of range")
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
            result.append(0)
    return result
