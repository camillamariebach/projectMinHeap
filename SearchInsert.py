# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 08:53:30 2020

@author: Tora
"""

def treeSearch(T, k):
    if  T==None or k==T[0]:
        return T
    if k< T[0]:
        return treeSearch(T[1], k)
    else: return treeSearch(T[2], k)

def iterativeTreeSearch (T, k):
    while T != None and k != T[0]:
        if k < T[0]:
            T = T[1]
        else: T = T[2]
    return T

def treeInsert (T, k):
    y = None
    x = T[0]
    
    while x != None:
        y = x
        if k[0] < x[0]:
            x = x[1]
        else: x = x[2]
        
    #!!! hvad er p??
    k.p = y
    
    if y == None:
        T[0]=k
    elif k[0] < y[0]:
        y[1] = k
    else: y[2] = k
    
def orderedTraversal(T):
    inorderTreewalk(T[0])

def inorderTreewalk(T):
    if T[0] != None: 
        inorderTreewalk(T[1])
        print(T[0])
        inorderTreewalk(T[2])
    