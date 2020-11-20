lst2 = []


def max_value(lst):
    for i in lst:
        if type(i) == list:
            max_value(i)
        else:
            lst2.append(i)
    return max(lst2)


lst = [12, 21, [32, 41, [15, 18]], 18, 19]
print(max_value(lst))
