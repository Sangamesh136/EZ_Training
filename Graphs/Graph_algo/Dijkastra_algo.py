G=[
    [0,  4, False, 7, False, False,False, 2, False, False],
    [4,  0,  5,  False, 3,  False, False,False, False, False],
    [False, 5,  0, 9, False, False, False, False, False, False],
    [7, False, 9,  0,  False,  False,  False, False, 6, False],
    [False, 3,False,  False,  0, 2, False, False,  7, False],
    [False, False, False,  False, 2,  0, False, False, False,8],
    [False,False, False,  1, False, False,  0, False,  False, 4],
    [2, False,  False,  False,  False, False, False,  0, False,6],
    [False,False, False, 6,  7, False,  False, False,  0,False],
    [False,  False, False, False, False, 8,  4, 6, False, 0]
]
temp={}
for i in range(len(G)):
    temp[i]=float("inf")
dist=[float("inf")]*len(G)
temp[0]=0

while len(temp)>0:
    min_value=min(temp.values())
    min_key=min(temp,key=temp.get)
    temp.pop(min_key)
    dist[min_key]=min_value
    for j in range(len(G[min_key])):
        if G[min_key][j]!=False and G[min_key][j]!=0:
            new_dist=min_value+G[min_key][j]
            if j in temp.keys() and temp[j]>new_dist:
                temp[j]=new_dist
print(dist)