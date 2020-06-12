# Better Implementation

def find_mother_vertex(g):
    last_vert = 0
    visited = [False] * g.vertices
    for x in range(g.vertices):
        if visited[x] is False:
            dfs(x, g, visited)
            last_vert = x
    # note: if graph not connected would need to do another dfs to verify
    return last_vert


def dfs(x, g, visited):
    stack = MyStack()
    stack.push(x)
    visited[x] = True
    while stack.is_empty() is False:
        cur = stack.pop()
        head = g.array[cur].head_node
        while head != None:
            if visited[head.data] is False:
                visited[head.data] = True
                stack.push(head.data)
            head = head.next_element


# Naive Implementation: Do dfs for each vertex
# def find_mother_vertex(g):
#     num_of_vertices_reached = 0
#     for i in range(g.vertices):
#         num_of_vertices_reached = perform_DFS(g, i)
#         if (num_of_vertices_reached is g.vertices):
#             return i
#     return - 1


# def perform_DFS(g, source):
#     num_of_vertices = g.vertices
#     vertices_reached = 0
#     visited = [False] * num_of_vertices
#     stack = MyStack()
#     stack.push(source)
#     visited[source] = True
#     while (stack.is_empty() is False):
#         current_node = stack.pop()
#         temp = g.array[current_node].head_node
#         while (temp is not None):
#             if (visited[temp.data] is False):
#                 stack.push(temp.data)
#                 visited[temp.data] = True
#                 vertices_reached += 1
#             temp = temp.next_element
#     return vertices_reached + 1
