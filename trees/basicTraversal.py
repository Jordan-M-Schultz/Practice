def createTree():
    node = Node(1)
    node.left = Node(2)
    node.right = Node(3)
    node.left.left = Node(4)
    node.left.right = Node(5)
    node.right.left = Node(6)
    node.right.right = Node(7)

    return node

def preorder(root):
    if(root is not None):
        print(root.data)
        preorder(root.left)
        preorder(root.right)

def levelOrder(root):
    queue = []
    queue.append(root)
    while(len(queue) != 0):
        node = queue.pop(0)
        print(node.data)
        
        queue.append(node.left) if node.left != None else ''
        queue.append(node.right) if node.left != None else ''


class Node: 
    left = None 
    right = None
    data = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return '%s' % self.data


tree = createTree()
levelOrder(tree)