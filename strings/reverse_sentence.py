def reverse_words(arr):
    start = None
    reverseWord(0, len(arr)-1, arr)
    for x in range(len(arr)):
        if start is None and arr[x] != " ":
            start = x
        elif arr[x] == " " and start != None:
            reverseWord(start, x-1, arr)
            start = None
        elif x == len(arr) - 1 and start != None:
            reverseWord(start, x, arr)
    return arr


def reverseWord(p1, p2, arr):
    if p2 is None:
        return
    while (p1 < p2):
        temp = arr[p1]
        arr[p1] = arr[p2]
        arr[p2] = temp
        p1 += 1
        p2 -= 1
