"""
@author: Tora de Boer
@author: toboe@student.sdu.dk
@author: Camilla Marie Bach
@author: cabac19@student.sdu.dk
"""

import sys
from ClassDictBinTree import DictBinTree

T = DictBinTree()

for line in sys.stdin:
    DictBinTree.insert(T,int(line))

DictBinTree.orderedTraversal(T)

#DictBinTree.inorderTreewalk()