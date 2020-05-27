from Queue import myQueue
from Stack import myStack


def reverseK(queue, k):
    if queue.isEmpty() or k > queue.size() or k < 0:
        return None

    stack = myStack()
    size = queue.size()

    for x in range(k):
        stack.push(queue.dequeue())

    while stack.isEmpty() is False:
        queue.enqueue(stack.pop())

    for x in range(size-k):
        queue.enqueue(queue.dequeue())
    return queue

# note: two pointers solution is more effient, but this is just to
# practice with stacks and queues
