"""
Camilla Marie Bach - cabac19@student.sdu.dk
Tora de Boer - toboe19@student.sdu.dk
"""
"""Class dictBinTree"""
from binNode import BinNode

class DictBinTree():
    """A class to represent a binary tree"""

    def __init__(self):
        self.root = None

    """Methods for class dictBinTree"""

    def inSearch(x, k, b):
        if k == x.key:
            b = True
        elif k < x.key:
            DictBinTree.inSearch(x.left, k, b)
        else:
            DictBinTree.inSearch(x.right, k, b)
        return b
        
    def search(T, k):
        b = False
        print(DictBinTree.inSearch(T.root, k, b))

    def insert(T, k):
        y = None
        x = T.root
        newNode = BinNode(k)
    
        #Find empty child node
        while x is not None:
            y = x
            if newNode.key < x.key:
                x = x.left
            else: 
                x = x.right

        #If no child node is found, set root to k         
        if y == None:
            T.root = newNode
        elif newNode.key < y.key:
            y.left = newNode
        else: y.right = newNode

    def inorderTreewalk(x):
        if x != None: 
            DictBinTree.inorderTreewalk(x.left)
            print(x.key)
            DictBinTree.inorderTreewalk(x.right)    
        
    def orderedTraversal(T):
        DictBinTree.inorderTreewalk(T.root)

