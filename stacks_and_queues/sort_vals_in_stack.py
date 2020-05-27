from Stack import myStack


def sortStack(stack):
    other_stack = myStack()
    other_stack.push(stack.pop())
    while stack.isEmpty() is False:
        cur = stack.pop()
        if other_stack.top() is not None and cur >= int(other_stack.top()):
            other_stack.push(cur)
        else:
            while other_stack.isEmpty() is False:
                stack.push(other_stack.pop())
            other_stack.push(cur)
    while other_stack.isEmpty() is False:
        stack.push(other_stack.pop())
    return stack


stacky = myStack()
stacky.push(19)
stacky.push(9)
stacky.push(9)
stacky.push(90)

sortStack(stacky)
