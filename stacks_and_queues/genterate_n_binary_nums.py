from Queue import myQueue


def findBin(number):
    results = []
    queue = myQueue()
    queue.enqueue(1)
    for x in range(0, number):
        results.append(str(queue.dequeue()))
        num1 = results[x] + "0"
        num2 = results[x] + "1"
        queue.enqueue(num1)
        queue.enqueue(num2)
    return results


print(findBin(3))
