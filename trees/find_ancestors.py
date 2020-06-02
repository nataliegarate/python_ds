def findAncestors(root, k):
    results = []

    def passPath(root, k):
        if root == None:
            return None
        if root.val == k:
            return True
        if root.val > k:
            result = passPath(root.leftChild, k)
        if root.val < k:
            result = passPath(root.rightChild, k)
        if result != None:
            results.append(root.val)
            return True
        return None

    passPath(root, k)
    return results
