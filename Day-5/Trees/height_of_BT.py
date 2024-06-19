class TreeNode:
    def __init__(self,value):
        self.value = value
        self.right = None
        self.left = None

def height(node):
    if node == None:
        return 0
    lh = height(node.left)
    rh = height(node.right)
    return (max(lh,rh)+1)
if __name__ == '__main__':
    node = TreeNode(1)

    node.left = TreeNode(2)
    node.right = TreeNode(3)

    node.left.left = TreeNode(4)
    node.left.right = TreeNode(5)
    node.right.left = TreeNode(6)
    node.right.right = TreeNode(7)

    # node.left.right.left = TreeNode(8)
    # node.left.right.right = TreeNode(9)
    # node.right.right.right = TreeNode(10)
    # node.left.right.left.left = TreeNode(11)
    # node.left.right.left.right = TreeNode(12)
    print(height(node))