def findSum(lst, k):
    map = {}
    for num in lst:
        map[num] = num
    for num in lst:
        desired_sum = k - num
        if desired_sum in map:
            return [desired_sum, num]
    return -1


print(findSum([1, 21, 3, 14, 5, 60, 7, 6], 81))
