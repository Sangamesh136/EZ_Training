def swap(lst, i, j):
    lst[i], lst[j] = lst[j], lst[i]

def find_pvt(lst):
    ptr = lst[0]
    i = 0
    j = len(lst)-1
    while i < j:
        while lst[i] <= ptr and i <= len(lst)-1:
            i += 1
        while lst[j] >= ptr and j >= 0:
            j -= 1
        if i < j:
            swap(lst,lst[i], lst[j])
    swap(ptr, lst[j])
    return j
def quick_sort(lst):
    if len(lst) <= 1:
        return lst
    pi = find_pvt(lst)
    quick_sort(lst[:pi])
    quick_sort(lst[pi:])
    return lst

lst = [4, 6, 2, 5, 7, 9, 1, 3]
#     [4, 3, 2, 5, 7, 9, 1, 6]
#     [4, 3, 2, 1, 7, 9, 5, 6]

print(quick_sort(lst))