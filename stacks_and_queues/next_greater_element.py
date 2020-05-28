from Stack import myStack


def nextGreaterElement(lst):
    returnArr = [-1] * len(lst)
    stack = myStack()
    for x in range(len(lst)):
        cur = lst[x]
        while stack.isEmpty() is False and lst[stack.top()] < cur:
            returnArr[stack.top()] = cur
            stack.pop()
        stack.push(x)
    return returnArr
