class TreeNode:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


def zig_zag(node):
    lst = []
    if node == None:
        return lst
    queue = [node]
    ptr = 0
    while len(queue) > 0:
        current_lst = []
        current_lst_size = len(queue)
        ptr += 1
        for i in range(current_lst_size):
            if ptr % 2 == 0:
                current_node = queue.pop(0)
                current_lst.append(current_node)
                if current_node.right != None:
                    queue.append(current_node.right)
                if current_node.left != None:
                    queue.append(current_node.left)

            else:
                current_node = queue.pop()
                current_lst.append(current_node.value)
                if current_node.left != None:
                    queue.insert(0, current_node.left)
                if current_node.right != None:
                    queue.insert(0, current_node.right)
        lst.append(current_lst)
    return lst

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
    print(zig_zag(node))