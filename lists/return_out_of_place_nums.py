def two_out_of_place_nums(lst):
    num1 = None
    num2 = None
    for i in range(1, len(lst)):
        if lst[i-1] > lst[i] and num1 == None:
            num1 = lst[i-1]
        if lst[i-1] > lst[i] and num1 != None:
            num2 = lst[i]
    return [num1, num2]


print(two_out_of_place_nums([1, 0, 2]))
print(two_out_of_place_nums([4, 2, 1]))

# the num that is too large will always come before the nums that is too small
# there will always be a num that is too large and too small

# note: could also traverse from front of array, and find single element
# where number is not smaller than one after it
# then traverse from back of array, and find single number that is
# not larger than the one before it
