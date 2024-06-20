
def DFS_helper(graph_dict, visited, element, stack):

    if visited[element] == False:
        stack.append(element)
        visited[element] = True

    else:
        return
    for i in graph_dict[element]:
        DFS_helper(graph_dict, visited, i[1], stack)
    print(stack.pop(), end= " ")

def DFS(graph_dict):

    visited = {}
    for i in graph_dict.keys():
        visited[i] = False
    stack = []
    element = graph_dict[1]
    DFS_helper(graph_dict, visited, 1, stack)

graph_dict = {
    1: [(1, 2, 0), (1, 3, 0)],
    2: [(2, 1, 0), (2, 7, 0)],
    3: [(3, 1, 0), (3, 6, 0), (3, 5, 0)],
    4: [(4, 7, 0), (4, 8, 0)],
    5: [(5, 3, 0), (5, 7, 0)],
    6: [(6, 3, 0), (6, 8, 0)],
    7: [(7, 2, 0), (7, 5, 0), (7, 4, 0)],
    8: [(8, 6, 0), (8, 4, 0)]
}
print("DFS of the graph:")
DFS(graph_dict)