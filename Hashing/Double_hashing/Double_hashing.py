dict_ = {}
global hash_lst
hash_lst = []

def hash_lstSize(lst):
   global hash_lst
   hash_lst= [None]*len(lst)
def hash(e):
    n = 11
    m = 8
    collision = 0
    h1 = h2 = h = 0
    h1 = e % 11
    if h1 in dict_:
        collision += 1
    h2 = 8 - (h1 % 8)
    if h2 in dict_:
        collision +=1
    h = (h1 + collision * h2) % 11
    while h in dict_:
        collision +=1
        h = (h1 + collision* h2) % 11

    dict_[h] = e


def hashTable(e):
    collision = 0
    n = 11
    m = 8
    h1 = e % n
    if hash_lst[h1]:
        collision +=1
    h2 = 8 - (e % 8)
    h = (h1 + collision * h2) % 11
    if hash_lst[h]:
        collision +=1
    h = (h1 + collision* h2)% 11
    while hash_lst[h] is not None:
        collision += 1
        h = (h1 + collision * h2) % 11
    hash_lst[h] = e

lst = [20, 34, 45, 70, 56, 81, 104, 37, 46, 39]
hash_lstSize(lst)
for i in lst:
    # hash(i)
    hashTable(i)
# print(dict_)
print(hash_lst)