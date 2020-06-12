from Graph import Graph
from Queue import MyQueue


def bfs_traversal(g, source):
    result = ""
    num_of_vertices = g.vertices
    visited = [False] * num_of_vertices
    queue = MyQueue()
    queue.enqueue(source)
    while queue.is_empty() is False:
        cur = queue.dequeue()
        visited[cur] = True
        result += str(cur)
        head = g.array[cur].get_head()
        while head != None:
            print(head.data)
            if (visited[head.data] is False):
                queue.enqueue(head.data)
            head = head.next_element
    return result
