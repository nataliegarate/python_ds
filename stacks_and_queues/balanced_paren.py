from Stack import myStack


def isBalanced(exp):
    stack = myStack()
    map = {'{': '}', '[': ']', '(': ')'}
    for char in exp:
        if char in map:
            stack.push(char)
        else:
            if char == map[stack.top()]:
                stack.pop()
            else:
                return False

    return stack.size() is 0
