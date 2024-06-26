class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = build_graphDict(edges)
def build_graphDict(edges):
    graph_dict = {}
    for start, end in edges:
        if start in graph_dict:
            graph_dict[start].append(end)
        else:
            graph_dict[start] = [end]
    return graph_dict


if __name__ == "__main__":
    routes = [
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris","Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto")
    ]
    graph_cls = Graph(routes)
    print(graph_cls.graph_dict)
