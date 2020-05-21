def findSecondMaximum(lst):
    if len(lst) < 2:
        return 'list too short'
    highest = second = float('-inf')
    for x in range(0, len(lst)):
        print(lst[x])
        if lst[x] > highest:
            temp = highest
            highest = lst[x]
            second = temp
        elif lst[x] > second and lst[x] != highest:
            second = lst[x]
        print(highest, second)
    if (second == float('-inf')):
        return 'only one unique value'
    return second


print(findSecondMaximum([0, 1080, 3, 89, 999]))

# alt
# def findSecondMaximum(lst):
#     lst.sort()
#     return lst[len(lst)-2]
