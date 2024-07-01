P = [5, 10, 15, 7, 8, 9, 4]
W = [1, 3, 4, 5, 4, 1, 3, 2]

P_W = {}
for i in range(len(P)):
    P_W[i] = P[i]/W[i]

print(P_W)

L = list(P_W.items())
Sorted_lst = sorted(L, reverse=True)
print(Sorted_lst)