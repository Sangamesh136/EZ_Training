def merge(left, right):
    li = ri = 0
    temp = []
    while li<len(left) and ri < len(right):
        if left[li] < right[ri]:
            temp.append(left[li])
            li +=1
        else:
            temp.append(right[ri])
            ri +=1
    while li < len(left):
        temp.append(left[li])
        li +=1
    while ri < len(right):
        temp.append(right[ri])
        ri += 1
    return temp

def merge_sort(lst):
    if len(lst) <=1:
        return lst
    # start = 0
    # end = len(lst)
    mid = len(lst)//2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    return merge(left,right)

lst = [4,3,1,2,5,7,9,8]
print(merge_sort(lst))

#  Time complexity O(NlogN)
#  Space complexity O(N)