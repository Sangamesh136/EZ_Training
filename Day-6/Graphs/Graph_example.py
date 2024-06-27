# class Graph:
#     def __init__(self, edges):
#         self.edges = edges
#         self.graph_dict = build_graphDict(edges)
# def build_graphDict(edges):
#     graph_dict = {}
#     for start, end in edges:
#         if start in graph_dict:
#             graph_dict[start].append(end)
#         else:
#             graph_dict[start] = [end]
#     return graph_dict


# if __name__ == "__main__":
#     routes = [
#         ("Mumbai", "Paris"),
#         ("Mumbai", "Dubai"),
#         ("Paris", "Dubai"),
#         ("Paris", "New York"),
#         ("Dubai", "New York"),
#         ("New York", "Toronto")
#     ]
#     graph_cls = Graph(routes)
#     print(graph_cls.graph_dict)

def adjecency_matrix(n,edges):
    matrix = [[0]*n for _ in range(n)]
    for start, end in edges:
        matrix[start][end] = 1
        matrix[end][start] = 1
    return matrix
n = 5
edges = [(0,1), (1, 2), (2,3), (3, 4)]
matrix = adjecency_matrix(n,edges)
for items in matrix:
    print(items)
