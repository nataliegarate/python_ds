def find_mother_vertex(g):
    num_of_vertices_reached = 0
    for i in range(g.vertices):
        num_of_vertices_reached = perform_DFS(g, i)
        if (num_of_vertices_reached is g.vertices):
            return i
    return - 1


def perform_DFS(g, source):
    num_of_vertices = g.vertices
    vertices_reached = 0
    visited = [False] * num_of_vertices
    stack = MyStack()
    stack.push(source)
    visited[source] = True
    while (stack.is_empty() is False):
        current_node = stack.pop()
        temp = g.array[current_node].head_node
        while (temp is not None):
            if (visited[temp.data] is False):
                stack.push(temp.data)
                visited[temp.data] = True
                vertices_reached += 1
            temp = temp.next_element
    return vertices_reached + 1
