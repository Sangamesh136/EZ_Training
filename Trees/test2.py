# traversal
class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

def insert(root,value):
    if root is None:

        return Node(value)
    if value > root.value:
        root.right = insert(root.right, value)
    elif value < root.value:
        root.left = insert(root.left, value)

    return root
# Deapth first search:
def inOrder(root):
    if root is None:
        return
    inOrder(root.left)
    print(root.value, end=" ")

    inOrder(root.right)

def preOrder(root):
     if root is None:
         return
     print(root.value, end=" ")

     preOrder(root.left)
     preOrder(root.right)

def postOrder(root):
    if root is None:
        return
    preOrder(root.left)
    preOrder(root.right)
    print(root.value, end=" ")

def level_orderTraversal(root):
    lst = []
    if root is None:
        return lst
    queue = []
    queue.append(root)
    while len(queue)> 0:
        inner_lst = []
        for i in range(len(queue)):
            current_e = queue.pop(0)
            inner_lst.append(current_e.value)
            if current_e.left is not None:
                queue.append(current_e.left)
            if current_e.right is not None:
                queue.append(current_e.right)
        lst.append(inner_lst)
    return lst




lst = [4, 6, 7, 3, 8, 2, 5, 9, 1]
root = Node(lst[0])

for i in range(1, len(lst)):
    root = insert(root,lst[i])
# inOrder(root)
# print()
# preOrder(root)
# print()
# postOrder(root)
print(level_orderTraversal(root))