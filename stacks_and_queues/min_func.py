from Stack import myStack
# Create Stack => stack = myStack(5); where 5 is size of stack
# Create Queue => queue = myQueue(5); where 5 is size of queue
# Stack Functions => isEmpty(), isFull(), top()
# Queue Functions => enqueue(int),dequeue(),isEmpty(),getSize()


class minStack:
    # Constructor
    def __init__(self):
        self.orderStack = myStack()
        self.mainStack = myStack()
        return None
        # Removes and return value from newStack

    def pop(self):
        # Write your code here
        if self.mainStack.isEmpty() is False:
            self.orderStack.pop()
            return self.mainStack.pop()
        else:
            return -1

        # Pushes values into newStack
    def push(self, value):
        self.mainStack.push(value)
        if self.orderStack.isEmpty() is False and self.orderStack.top() < value:
            self.orderStack.push(self.orderStack.top())
        else:
            self.orderStack.push(value)

    def min(self):
        if self.orderStack.isEmpty() is False:
            return self.orderStack.top()
        return -1
