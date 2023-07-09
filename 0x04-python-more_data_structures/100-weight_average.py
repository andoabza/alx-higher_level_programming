#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == 0:
        return 0
    else:
        for g in range(len(my_list)):
        rate[g] = my_list[g] * (amount[g] / sum(amount))
        my_list = sum(rate)
        return my_list
