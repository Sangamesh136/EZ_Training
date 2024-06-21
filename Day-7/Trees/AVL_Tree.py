# def inOrder(node):
#     if node == None:
#         return
#     inOrder(node.left)
#     print(node.value, end=" ")
#     inOrder(node.right)
#
#
# def insert_AVL(node, value):
#     if node == None:
#         return Node(value)
#     if value > node.value:
#         node.right = insert_AVL(node.right, value)
#
#     if value < node.value:
#         node.left = insert_AVL(node.left, value)
#     node.height = 1 + max(height(node.left), height(node.right))
#     BF = getBF(node)
#
#     if BF > 1 and value < node.left.value:
#         return rightRotate(node)
#
#     if BF > 1 and value > node.left.value:
#         node.left = leftRotate(node.left)
#         return rightRotate(node)
#
#     if BF < -1 and value > node.right.value:
#         return leftRotate(node)
#
#     if BF < -1 and value < node.right.value:
#         node.right = rightRotate(node.right)
#         return leftRotate(node)
#
#     return node
#
#
# def height(node):
#     if node is None:
#         return 0
#     # return max(height(node.left), height(node.right)) + 1
#     return node.height
#
#
# def getBF(node):
#     if node is None:
#         return 0
#     return height(node.left) - height(node.right)
#
#
# def rightRotate(A):
#     B = A.left
#     temp = B.right
#     B.right = A
#     A.left = temp
#     A.height = 1 + max(height(A.left), height(A.right))
#     B.height = 1 + max(height(B.left), height(B.right))
#     return B
#
#
#
# def leftRotate(A):
#     B = A.right
#     temp = B.left
#     B.left = A
#     A.right = temp
#     A.height = 1 + max(height(A.left), height(A.right))
#     B.height = 1 + max(height(B.left), height(B.right))
#     return B
#
#
# class Node:
#     def __init(self, value):
#         self.value = value
#         self.left = None
#         self.right = None
#         self.height = 1
#
#
# if __name__ == '__main__':
#     node = None
#     VL = [19, 99, 75, 7, 21, 34, 38, 27, 134, 100, 29, 0, 12, 17, 143]
#     for i in VL:
#         node = insert_AVL(node, i)
#     inOrder(node)


class node:
    def _init_(self, data):
        self.val = data
        self.left = None
        self.right = None
        self.height = 1


def insert(root, super):
    if root == None:
        return node(super)
    if super < root.val:
        root.left = insert(root.left, super)
    else:
        root.right = insert(root.right, super)
    root.height = 1 + max(ght(root.left), ght(root.right))
    BF = getBF(root)
    # RR rotation
    if BF > 1 and super < root.left.val:
        return rightRotate(root)
    # RL rotation
    if BF > 1 and super > root.left.val:
        root.left = leftRotate(root.left)
        return rightRotate(root)
    # LR Rotation
    if BF < -1 and super < root.right.val:
        root.right = rightRotate(root.right)
        return leftRotate(root)
    # LL rotation
    if BF < -1 and super > root.right.val:
        return (leftRotate(root))
    return root


def ght(root):
    if root == None:
        return 0
    return root.height


def getBF(root):
    if not root:
        return 0
    return ght(root.left) - ght(root.right)


def leftRotate(A):
    B = A.right
    temp = B.left
    B.left = A
    A.right = temp

    A.height = 1 + max(ght(A.left), ght(A.right))
    B.height = 1 + max(ght(B.left), ght(B.right))

    return B


def rightRotate(A):
    B = A.left
    temp = B.right
    B.right = A
    A.left = temp

    A.height = 1 + max(ght(A.left), ght(A.right))
    B.height = 1 + max(ght(B.left), ght(B.right))

    return B


def inorder(root):
    if root == None:
        return
    inorder(root.left)
    print(root.val, end=" ")
    inorder(root.right)


def postorder(root):
    if not root:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.val, end=" ")


if __name__ == "__main__":
    root = None
    vl = [19, 99, 75, 7, 21, 34, 38, 27, 134, 100, 29, 0, 12, 17, 143]
    for i in vl:
        root = insert(root, i)
    inorder(root)
    # postorder(root)