#  Kraden's Algorithm

lst = [4, -1, -3, 6, -2, -1, 3, 2, -8, -2]
summ = 0
maxi = 0
for i in range(len(lst)):
    summ += lst[i]
    if maxi < summ:
        maxi = summ
    if summ < 0:
        summ = 0

print(maxi)

