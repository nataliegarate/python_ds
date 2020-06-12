def detect_cycle(g):
    stack = MyStack()
    visited = [False] * g.vertices
    stack.push(0)
    while stack.is_empty() is False:
        cur = stack.pop()
        visited[cur] = True
        head = g.array[cur].head_node
        while head != None:
            if visited[head.data] == True:
                return True
            else:
                stack.push(head.data)
            head = head.next_element
    return False
