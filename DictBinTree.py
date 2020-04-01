"""
@author: Tora de Boer
@author: toboe@student.sdu.dk
@author: Camilla Marie Bach
@author: cabac19@student.sdu.dk
"""

def search(T, k):
    found = False
    if k==T[0]:
        found = True
    return found
    if k< T[0]:
        return search(T[1], k)
    else: return search(T[2], k)

def iterativeTreeSearch (T, k):
    while T[0] != None and k != T[0]:
        if k < T[0]:
            T = T[1]
        else: T = T[2]
    return T

def insert(T, k):
    y = None
    x = T[0]
    k = [k, None, None]
    print('T:')
    print(T)
    
    while x != None:
        y = x
        if k < T[0]:
            x = T[1]
        else: x = T[2]
        
    #!!! hvad er p??
    #k.p = y
    
    if y == None:
        T[0]=k
    elif k < y[0]:
        y[1] = k
    else: y[2] = k
    
def orderedTraversal(T):
    inorderTreewalk(T[0])

def inorderTreewalk(T):
    orderedlist = []
    if T[0] != None: 
        inorderTreewalk(T[1])
        orderedlist.append(T[0])
        inorderTreewalk(T[2])
    