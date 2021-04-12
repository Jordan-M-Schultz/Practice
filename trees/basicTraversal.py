from node import Node
import math

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
        queue.append(node.right) if node.right != None else ''

def zigZag(root): # assumption binary tree
    right = True
    current = []
    after = []
    current.append(root)
    
    while(len(current) != 0):
        node = current.pop(len(current) - 1)
        print(node.data)

        if right:
            after.append(node.left) if node.left != None else ''
            after.append(node.right) if node.right != None else ''
        else:
            after.append(node.right) if node.right != None else ''
            after.append(node.left) if node.left != None else ''
        
        if len(current) == 0:
            right = not right 
            current = after
            after = []


def minTree(array, start, end):
    '''
        Given a sorted array with unique integers, create a bst with min height
    '''
    if start > end : 
        return None
    
    mid = math.ceil((start + end)/2)
    
    node = Node(array[mid])
    node.left = minTree(array, start, mid-1)
    node.right = minTree(array, mid+1, end)

    return node
        





tree = createTree()
# zigZag(tree)
root = minTree([4,5,6,7,8,9], 0, 5)

levelOrder(root)