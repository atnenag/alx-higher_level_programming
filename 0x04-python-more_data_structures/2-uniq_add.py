#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_list2 = []
    total = 0
    for m in my_list:
        if m not in my_list2:
            my_list2.append(m)
    return sum(my_list2)
