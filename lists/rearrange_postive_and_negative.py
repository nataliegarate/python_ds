def rearrange(lst):
    p1 = 0
    p2 = len(lst)-1
    while p1 < p2 and p1 >= 0 and p2 <= len(lst) - 1:
        if lst[p1] < 0 and lst[p2] >= 0:
            p1 += 1
            p2 -= 1
        # p1 is good but p2 isnt
        elif lst[p1] < 0 and lst[p2] < 0:
            p1 += 1
        # p2 is good, but p1 isn't
        elif lst[p1] >= 0 and lst[p2] >= 0:
            p2 -= 1
        elif lst[p1] >= 0 and lst[p2] < 0:
            temp = lst[p1]
            lst[p1] = lst[p2]
            lst[p2] = temp
            p1 += 1
            p2 -= 1
    return lst


print(rearrange([-1, 2, -3, -4, 5]))
print(rearrange([0, 0, 0, -2]))
