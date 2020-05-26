import math


def maxMin(lst):
    mid = math.floor(len(lst) / 2)
    asc = lst[0:mid]
    desc = lst[mid:len(lst)]
    ascIdx = 0
    descIdx = len(desc)-1
    for x in range(0, len(lst)):
        if x % 2 == 0:
            lst[x] = desc[descIdx]
            descIdx -= 1
        else:
            lst[x] = asc[ascIdx]
            ascIdx += 1
    return lst


maxMin([1, 2, 3, 4, 5, 6])
maxMin([1, 2, 3, 4, 5])
