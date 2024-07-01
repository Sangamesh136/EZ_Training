#  Kraden's Algorithm

lst = [1, 2, 3, -2, 5]
summ = 0
maxi = 0
for i in range(len(lst)):
    summ += lst[i]
    if maxi < summ:
        maxi = summ
    if summ < 0:
        summ = 0

print(maxi)

