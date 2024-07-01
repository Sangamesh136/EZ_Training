def insert(root, value):
    if root == None:
        return Node(value)
    if root.value > value:
        root.left = insert(root.left, value)
    if root.value < value:
        root.right = insert(root.right, value)
    # if root.value == value:
    #     return
    return root


def inOrder(root):
    if root == None:
        return
    inOrder(root.left)
    print(root.value)

    inOrder(root.right)


class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


lst = [4, 6, 7, 3, 8, 2, 5, 9, 1]
root = Node(lst[0])
for i in range(1, len(lst)):
    insert(root, lst[i])
inOrder(root)
