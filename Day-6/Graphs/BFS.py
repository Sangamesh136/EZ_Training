def BFS(graph_dict,e):
    Q = [e]
    v = {}
    for i in graph_dict.keys():
        v[i] = False
    v[e] = True
    while len(Q) != 0:
        curr = Q.pop(0)
        print(curr)
        for i in graph_dict[curr]:
            if v[i[1]] == False:
                Q.append(i[1])
                v[i[1]] = True

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
print("BFS of the graph:")
BFS(graph_dict, 1)