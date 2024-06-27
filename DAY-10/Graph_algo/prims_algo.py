import math

if __name__ == "__main__":
    # graph_dict = {
    #     1: [(1, 2, 7), (1, 8, 2)],
    #     2: [(2, 1, 7), (2, 6, 5), (2, 4, 1), (2, 3, 4)],
    #     3: [(3, 2, 4), (3, 8, 8)],
    #     4: [(4, 2, 1), ()]
    # }

    graph_matrix = [
        [0, 7, -1, -1, -1, -1, -1, -1, -1, -1],
        [7, 0, 4, 1, -1, 5, -1, -1, -1, -1],
        [-1, 4, 0, -1, -1, -1, -1, 8, -1, -1],
        [-1, 1, -1, 0, 6, 8, 3, 3, -1, -1],
        [-1, -1, -1, 6, 0, -1, -1, 6, 8, -1],
        [-1, 5, -1, 8, -1, 0, -1, -1, -1, -1],
        [-1, -1, -1, 3, -1, -1, 0, -1, -1, -1],
        [2, -1, 8, 3, 6, -1, -1, 0, -1, -1],
        [-1, -1, -1, 1, 8, -1, 9, -1, 0, -1],
        [-1, -1, -1, -1, -1, -1, 2, -1, -1, 0]
    ]
    visited = [False] * len(graph_matrix)

    mini = float('inf')
    current_mini = math.inf
    x = 0
    y = 0
    for i in range(len(graph_matrix)):
        for j in range(len(graph_matrix[i])):
            if graph_matrix[i][j] > 0:
                if graph_matrix[i][j] < current_mini:
                    current_mini = graph_matrix[i][j]
                    x = i
                    y = j
        if current_mini < mini:
            mini = current_mini
            # x = i
            # y = j
    # print(x + 1, y + 1, mini)

    visited[x] = True
    visited[y] = True
    T = []
    T.append(tuple((x + 1, y + 1, mini)))
    # print(T)
    x = y = 0
    while False in visited:
        min = math.inf
        for i in range(len(visited)):
            if visited[i] == True:
                for j in range(len(graph_matrix[i])):
                    if graph_matrix[i][j] == 0 or graph_matrix[i][j] == -1 or visited[j] == True:
                        continue
                    elif min > graph_matrix[i][j]:
                        min = graph_matrix[i][j]
                        x = i
                        y = j
        visited[y] = True
        T.append(tuple((x+1, y+1, min)))
    print(T)
    # for i in T:
    #     print(i)