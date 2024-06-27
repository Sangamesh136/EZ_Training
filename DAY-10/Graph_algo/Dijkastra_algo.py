import math

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
mini_value = {}
for i in range(1, len(graph_matrix)+1):
    mini_value[i] = math.inf

# print(mini_value)
element_lst = []

mini_value[1] = 0
print(mini_value)
element_lst.append(mini_value.pop())