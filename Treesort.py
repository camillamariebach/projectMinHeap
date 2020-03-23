import sys
import DictBinTree

db = []

for line in sys.stdin:
    DictBinTree.insert(db,int(line))

print(DictBinTree.orderedTraversal(db))

def orderedTraversal(T):
    inorderTreewalk(T.root)

def inorderTreewalk(x):
    if x != None: 
        inorderTreewalk(x[1])
        print(x[0])
        inorderTreewalk(x[2])