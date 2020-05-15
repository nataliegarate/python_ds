def findMinimum(arr):
    if len(arr) == 0:
        return None
    min_val = arr[0]
    for num in arr:
        if num < min_val:
            min_val = num
    return min_val


def findMinimum2(arr):
    if len(arr) == 0:
        return None
    arr.sort()
    return arr[0]
