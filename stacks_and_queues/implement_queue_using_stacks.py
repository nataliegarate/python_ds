from Stack import myStack
# Create Stack => stack = myStack(5); where 5 is size of stack
# Push Function => stack.push(int)  //Inserts the element at top
# Pop Function => stack.pop()       //Removes and returns the element at top
# Top/Peek Function => stack.getTop()  //Returns top element
# Helper Functions => stack.isEmpty() & stack.isFull() //returns boolean


class newQueue:
    def __init__(self):
        self.mainStack = myStack()
        self.sideStack = myStack()
        # Write your code here

        # Inserts Element in the Queue
    def enqueue(self, value):
        self.mainStack.push(value)

    def dequeue(self):
        if self.sideStack.isEmpty() & self.mainStack.isEmpty():
            return None
        if self.sideStack.isEmpty():
            while self.mainStack.size() > 0:
                self.sideStack.push(self.mainStack.pop())

        return self.sideStack.pop()
