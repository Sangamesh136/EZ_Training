# class node:
#     def _init_(self, data):
#         self.val = data
#         self.left = None
#         self.right = None
#         self.height = 1
#
#
# def insert(root, super):
#     if root == None:
#         return node(super)
#     if super < root.val:
#         root.left = insert(root.left, super)
#     else:
#         root.right = insert(root.right, super)
#     root.height = 1 + max(ght(root.left), ght(root.right))
#     BF = getBF(root)
#     # RR rotation
#     if BF > 1 and super < root.left.val:
#         return rightRotate(root)
#     # RL rotation
#     if BF > 1 and super > root.left.val:
#         root.left = leftRotate(root.left)
#         return rightRotate(root)
#     # LR Rotation
#     if BF < -1 and super < root.right.val:
#         root.right = rightRotate(root.right)
#         return leftRotate(root)
#     # LL rotation
#     if BF < -1 and super > root.right.val:
#         return (leftRotate(root))
#     return root
#
#
# def ght(root):
#     if root == None:
#         return 0
#     return root.height
#
#
# def getBF(root):
#     if not root:
#         return 0
#     return ght(root.left) - ght(root.right)
#
#
# def leftRotate(A):
#     B = A.right
#     temp = B.left
#     B.left = A
#     A.right = temp
#
#     A.height = 1 + max(ght(A.left), ght(A.right))
#     B.height = 1 + max(ght(B.left), ght(B.right))
#
#     return B
#
#
# def rightRotate(A):
#     B = A.left
#     temp = B.right
#     B.right = A
#     A.left = temp
#
#     A.height = 1 + max(ght(A.left), ght(A.right))
#     B.height = 1 + max(ght(B.left), ght(B.right))
#
#     return B
#
#
# def inorder(root):
#     if root == None:
#         return
#     inorder(root.left)
#     print(root.val, end=" ")
#     inorder(root.right)
#
#
# def postorder(root):
#     if not root:
#         return
#     postorder(root.left)
#     postorder(root.right)
#     print(root.val, end=" ")
#
#
# if __name__ == "__main__":
#     root = None
#     vl = [19, 99, 75, 7, 21, 34, 38, 27, 134, 100, 29, 0, 12, 17, 143]
#     for i in vl:
#         root = insert(root, i)
#     inorder(root)
#     # postorder(root)

lst = [4, -1, -3, 6, -2, -1, 3, 2, -8, -2]
sum = 0
maxi = 0
for i in range(len(lst)):
    for j in range(i, len(lst)):

        sum += lst[j]
        if sum > maxi:
            maxi = sum

print(maxi)