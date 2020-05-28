from Stack import myStack


def evaluatePostFix(exp):
    stack = myStack()
    for char in exp:
        if char.isdigit():
            stack.push(char)
        else:
            right = stack.pop()
            left = stack.pop()
            res = str(eval(left + char + right))
            stack.push(res)
    return int(float(stack.pop()))
