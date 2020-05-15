# no extra space
def removeEven(List):
    num_of_evens = 0
    idx = 0
    for num in List:
        if num % 2 == 0:
            num_of_evens += 1
        else:
            List[idx - num_of_evens] = num
        idx += 1
    count = 0
    while count < num_of_evens:
        List.pop()
        count += 1
    return List


print(removeEven([1, 2, 3, 4]))


# returns a new list
def removeEven2(List):
    # List comprehension to iter aover List and add to new list if not even
    return [number for number in List if number % 2 != 0]
