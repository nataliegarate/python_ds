def findFirstUnique(lst):
    map = {}
    i = 0
    for num in lst:
        if num in map:
            map[num]["unique_first_index"] = None
        else:
            map[num] = {}
            map[num]["val"] = num
            map[num]["unique_first_index"] = i
        i += 1
    print(map)
    for val in map.values():
        if val["unique_first_index"] != None:
            return val["val"]
    return None


print(findFirstUnique([4, 5, 1, 2, 0, 4]))

# note: for older versions of python
# from collections import OrderedDict
# than  map = OrderedDict()
