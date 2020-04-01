"""
@author: Tora de Boer
@author: toboe@student.sdu.dk
@author: Camilla Marie Bach
@author: cabac19@student.sdu.dk
"""

import sys
import DictBinTree

T = [None]

for line in sys.stdin:
    DictBinTree.insert(T,int(line))

print(DictBinTree.orderedTraversal(T))