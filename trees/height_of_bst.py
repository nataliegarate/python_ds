def findHeight(root):
    def countHeight(root):
        if root is None:
            return 0
        return 1 + max(countHeight(root.leftChild), countHeight(root.rightChild))
    return countHeight(root) - 1
