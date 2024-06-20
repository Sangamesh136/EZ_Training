def preOrder(root):
    if root == None:
        return
    print(root.value)
    preOrder(root.left)
    preOrder(root.right)

def inOrder(root):
    if root == None:
        return
    inOrder(root.left)
    print(root.value)
    inOrder(root.right)

def postOrder(root):
    if root == None:
        return
    postOrder(root.left)
    postOrder(root.right)
    print(root.value)
class node:
    def __init__(self,data):
        self.value = data
        self.right = None
        self.left = None
    
if __name__ == "__main__":
    root = node(1)

    root.right = node(3)
    root.left = node(2)

    root.left.left = node(4)
    root.left.right = node(5) 
    root.right.left = node(6)
    root.right.right = node(7)
    print()
    preOrder(root)
    # print()
    # inOrder(root)
    # print()
    # postOrder(root)
    # print()
