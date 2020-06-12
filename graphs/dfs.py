def dfs_traversal(g, source):
    result = ""
    stack = MyStack()
    stack.push(source)
    visited = [False] * g.vertices
    while stack.is_empty() is False:
        cur = stack.pop()
        head = g.array[cur].head_node
        visited[cur] = True
        result += str(cur)
        while head != None:
            if visited[head.data] is False:
                stack.push(head.data)
            head = head.next_element
    return result
