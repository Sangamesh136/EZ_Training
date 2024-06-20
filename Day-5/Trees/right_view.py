class TreeNode:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


def rightView(node):
    if node == None:
        return
    queue = [node]
    while queue:
        current_level = len(queue)
        for i in range(current_level):
            current = queue.pop(0)
            if i == current_level - 1:
                print(current.value, end=" ")

            if current.left != None:
                queue.append(current.left)

            if current.right != None:
                queue.append(current.right)


if __name__ == '__main__':
    node = TreeNode(1)

    node.left = TreeNode(2)
    node.right = TreeNode(3)

    node.left.left = TreeNode(4)
    node.left.right = TreeNode(5)
    node.right.left = TreeNode(6)
    node.right.right = TreeNode(7)

    node.left.right.left = TreeNode(8)
    node.left.right.right = TreeNode(9)
    node.right.right.right = TreeNode(10)
    node.left.right.left.left = TreeNode(11)
    node.left.right.left.right = TreeNode(12)
    rightView(node)
