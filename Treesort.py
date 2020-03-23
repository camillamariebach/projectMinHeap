import sys
import DictBinTree

T = []

for line in sys.stdin:
    DictBinTree.insert(T,int(line))

print(DictBinTree.orderedTraversal(T))

def orderedTraversal(T):
    inorderTreewalk(T.root)

def inorderTreewalk(T):
    if T != None: 
        inorderTreewalk(T[1])
        print(T[0])
        inorderTreewalk(T[2])