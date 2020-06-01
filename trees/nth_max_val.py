def findKthMax(root, k):
    if k < 1:
        return None

    def traverseNodes(root, k, num):
        if root is None:
            return None
        right = traverseNodes(root.rightChild, k, num)
        if right != None:
            return right
        num[0] += 1
        if num[0] == k:
            return root.val
        else:
            return traverseNodes(root.leftChild, k, num)

    return traverseNodes(root, k, [0])
