greed = [1, 5, 3, 3, 4]
cookies = [4, 2, 1, 2, 1, 3]

greed.sort()        # [1, 3, 3, 4, 5]

cookies.sort()      # [1, 1, 2, 2, 3, 4]
print(greed)
print(cookies)
count = 0
i = 0
j = 0
while i <= len(greed):
    if greed[j] <= cookies[i]:
        j += 1
        count += 1
    i += 1

print(count)