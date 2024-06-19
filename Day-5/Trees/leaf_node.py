class TreeNode:
    def __init__(self,value):
        self.value = value
        self.right = None
        self.left = None

def leaf_node(node):
    if node.left == None and node.right == None:
        print(node.value, end = " ")
        return
    if node.left != None:
        leaf_node(node.left)
    if node.right != None:
        leaf_node(node.right)
if __name__ == '__main__':
    node = TreeNode(1)

    node.left = TreeNode(2)
    node.right = TreeNode(3)

    node.left.left = TreeNode(4)
    node.left.right = TreeNode(5)
    node.right.left = TreeNode(6)
    node.right.right = TreeNode(7)
    leaf_node(node)