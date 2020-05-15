def merge_lists(lst1, lst2):
    return_list = []
    p1 = 0
    p2 = 0
    while (p1 < len(lst1) and p2 < len(lst2)):
        if lst1[p1] < lst2[p2]:
            return_list.append(lst1[p1])
            p1 += 1
        else:
            return_list.append(lst2[p2])
            p2 += 1
    if p1 < len(lst1):
        return_list.extend(lst1[p1:])
    if p2 < len(lst2):
        return_list.extend(lst2[p2:])
    return return_list


print(merge_lists([1, 4, 5], [2, 4, 6]))

# note: can also be solved with insert functionailty which would increase time complexity but decrease space complexity
