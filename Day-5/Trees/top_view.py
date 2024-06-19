class node_data:
    def __init__(self,Node,HKey):
        self.node = Node
        self.hkey = HKey
    
def topview(node):
    temp = node_data(node,0)
    Q = [temp]
    Q.append(None)

    key_Dict = {}
    while len(Q) !=0:
        curr = Q.pop(0)

        if curr == None:
            if len(Q) == 0:
                break
            else:
                Q.append(None)
        else:
            if curr.hkey not in key_Dict.keys():
                key_Dict[curr.hkey] = curr.node.value
            
            if curr.node.left !=None:
                temp = node_data(curr.node.left,curr.hkey-1)
                Q.append(temp)
            if curr.node.right != None:
                temp = node_data(curr.node.right,curr.hkey+1)
                Q.append(temp)
    for i in sorted(key_Dict.keys()):
        print(key_Dict[i])
    print(key_Dict)
    # print(key_Dict)

class TreeNode:
    def __init__(self,value):
        self.value = value
        self.right = None
        self.left = None

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

    topview(node)