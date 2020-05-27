import numpy as np


class twoStacks:
    # Initialize the two stacks here
    def __init__(self, size):
        self.size = size
        self.stack = np.zeros([size], dtype=int)
        self.stack1_end = 0
        self.stack2_end = self.size - 1
    # Insert Value in First Stack

    def push1(self, value):
        if self.stack1_end == self.stack2_end:
            return 'stack overflow'
        self.stack[self.stack1_end] = value
        self.stack1_end += 1

    # Insert Value in Second Stack
    def push2(self, value):
        if self.stack1_end == self.stack2_end:
            return 'stack overflow'
        self.stack[self.stack2_end] = value
        self.stack2_end -= 1

    # Return and remove top Value from First Stack
    def pop1(self):
        if self.stack1_end != self.size - 1:
            temp = self.stack[self.stack1_end - 1]
            self.stack[self.stack1_end - 1] = 0
            self.stack1_end -= 1
            return temp
        else:
            return 'nothing to pop'
    # Return and remove top Value from Second Stack

    def pop2(self):
        if self.stack2_end != 0:
            temp = self.stack[self.stack2_end + 1]
            self.stack[self.stack2_end + 1] = 0
            self.stack2_end += 1
            return temp
        else:
            return 'nothing to pop'
