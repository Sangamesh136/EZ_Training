class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None
        self.height = 1


def insert_AVL(node, data):
    if node is None:
        return Node(data)
    if data > node.val:
        node.right = insert_AVL(node.right, data)
    if data < node.val:
        node.left = insert_AVL(node.left, data)

    node.height = max(height(node.left), height(node.right)) + 1

    return rotate(node)


def height(node):
    if node is None:
        return 0
    return node.height


def rotate(node):
    if height(node.left) - height(node.right) > 1:  # Left heavy
        if height(node.left.left) - height(node.left.right) > 0:
            return right_rotate(node)
        else:
            node.left = left_rotate(node.left)
            return right_rotate(node)

    if height(node.right) - height(node.left) > 1:
        if height(node.right.right) - height(node.right.left) > 0:
            return left_rotate(node)
        else:
            node.right = right_rotate(node.right)
            return left_rotate(node)

    return node

def right_rotate(A):
    B = A.left
    temp = B.right
    B.right = A
    A.left = temp

    A.height = max(height(A.left), height(A.right)) + 1
    B.height = max(height(B.left), height(B.right)) + 1
    return B


def left_rotate(A):
    B = A.right
    temp = B.left
    B.left = A
    A.right = temp

    A.height = max(height(A.left), height(A.right)) + 1
    B.height = max(height(B.left), height(B.right)) + 1
    return B


def inOrder(node):
    if node is None:
        return
    inOrder(node.left)
    print(node.val, end=" ")
    inOrder(node.right)


if __name__ == "__main__":
    vl = [19, 99, 75, 7, 21, 34, 38, 27, 134, 100, 29, 0, 12, 17, 143]
    vl.sort()
    root = None
    for i in vl:
        root = insert_AVL(root, i)
        # print(insert_AVL(root, i))
    inOrder(root)
    print()
    print(vl)

