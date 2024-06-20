# #  DFS
# def preOrder(node):
#     if node == None:
#         return
#     print(node.value, end= " ")
#     preOrder(node.left)
#     preOrder(node.right)

# def inOrder(node):
#     if node == None:
#         return 
#     inOrder(node.left)
#     print(node.value, end=" ")
#     inOrder(node.right)

# def postOrder(node):
#     if node == None:
#         return
#     postOrder(node.left)
#     postOrder(node.right)
#     print(node.value, end=' ')

# class TreeNode:
#     def __init__(self,value):
#         self.value = value
#         self.left = None
#         self.right = None
    
# if __name__ == "__main__":
#     root = TreeNode(1)
#     root.right = TreeNode(3)
#     root.left = TreeNode(2)
#     root.left.left = TreeNode(4)
#     root.left.right = TreeNode(5) 
#     root.right.left = TreeNode(6)
#     root.right.right = TreeNode(7)
#     preOrder(root)
#     print()
#     inOrder(root)
#     print()
#     postOrder(root)

# # Level order Traversal:
def BFS(node):
    Queue = [node]                          #[1]
    Queue.append(None)                      #[1, None]
    while len(Queue) > 0:
        current = Queue.pop(0)              #[None], popper = 1  | popped = None [2, 3]
        if current == None:                 # false              | True
            if len(Queue) == 0:             #                    | false
                break
            print()                         #                    | new line
            Queue.append(None)              #                    | [2,3,None]
        else:
            print(current.value, end=" ")   #print 1
            if current.left != None:        
                Queue.append(current.left)  # [None, 2]
            if current.right != None:
                Queue.append(current.right) # [None, 2, 3]
class TreeNode:
    def __init__(self,value):
        self.value = value
        self.right = None
        self.left = None

if __name__ == "__main__":
    root = TreeNode(1)
    root.right = TreeNode(3)
    root.left = TreeNode(2)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5) 
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    BFS(root)