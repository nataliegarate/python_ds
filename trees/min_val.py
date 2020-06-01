def findMin(root):
    if root is None:
        return None
    if root.leftChild == None:
        return root.val
    return findMin(root.leftChild)
