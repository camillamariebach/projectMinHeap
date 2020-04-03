"""Class dictBinTree"""
from binNode import BinNode

class DictBinTree():
    """A class to represent a binary tree"""

    def __init__(self):
        self.root = None

    """Methods for class dictBinTree"""

    def search(T, k):
        found = False
        if k == T.root:
            found = True
        if k < T.root:
            search(T.root.left, k)
        else: search(T.root.right, k)
        return found 

    def iterativeTreeSearch (T, k):
        while T[0] != None and k != T[0]:
            if k < T[0]:
                T = T[1]
            else: T = T[2]
        return T

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

