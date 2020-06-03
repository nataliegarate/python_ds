# iterative
def findKNodes(root, k):
    if root is None:
        return None

    def findKNodes(root, k):
        results = []
        queue = [{'node': root, 'order': 0}]
        while len(queue) > 0:
            cur = queue.pop(0)
            if cur['order'] == k:
                results.append(cur['node'].val)
                continue
            if (cur['node'].leftChild != None):
                queue.append(
                    {'node': cur['node'].leftChild, 'order': cur['order'] + 1})
            if (cur['node'].rightChild != None):
                queue.append(
                    {'node': cur['node'].rightChild, 'order': cur['order'] + 1})
        return results
    return findKNodes(root, k)

# recursive
# def findKNodes(root, k):
#     def addNodes(root, k, num, arr):
#         if root is None:
#             return arr
#         if k == num:
#             arr.append(root.val)
#             return arr
#         addNodes(root.leftChild, k, num + 1, arr)
#         addNodes(root.rightChild, k, num + 1, arr)
#         return arr
#     return addNodes(root, k, 0, [])
