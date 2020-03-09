import math
import random
import sys


def min_heapify(A, i):
    """Method that restores the properties of a min heap by recursively calling itself on the list""" 
    l = left(i)
    r = right(i)
    if l <= len(A)-1 and A[l] < A[i]:
        smallest = l
    else: 
        smallest = i
    if r <= len(A)-1 and A[r] < A[smallest]:
        smallest = r
    if smallest != i: 
        temp = A[smallest]
        A[smallest] = A[i]
        A[i] = temp
        min_heapify(A, smallest)

def extractMin(A):
    """Methods that extracts the minimum value in the heap and restores min heap properties""" 
    min = A[0]
    A[0] = A[len(A)-1]
    A.pop(len(A)-1)
    min_heapify(A, 0)
    return min

def heap_min(A):
    """Method that returns the minimum value, stored in the node A[0]"""
    return A[0]

def insert(A, e):
    """Method that inserts an element to the end of the list A, then swaps something around""" 
    A.append(e)
    i = len(A)-1
    while i > 0 and A[parent(i)] > A[i]:
        temp = A[parent(i)]
        A[parent(i)] = A[i]
        A[i] = temp
        i = parent(i)

def build_min_heap(A):
    """Method that builds a min heap by recursively calling min_heapify on an unordered list"""
    m = math.floor((len(A)-1) / 2)
    for i in range(m, -1, -1):
        min_heapify(A, i)

def heapsort(A):
    """Method that manages the heap-sort algorithm by first building a heap, then outputs the list in sorted order and restores min heap properteis""" 
    build_min_heap(A)
    end = len(A)-1
    for i in range(end, 1, -1): 
        temp = A[0]
        A[0] = A[i]
        A[i] = temp
        min_heapify(A, 0)
 
def parent(i):
    """Getter for the parent node of i""" 
    return math.floor((i-1)/2)

def left(i): 
    """Getter for the left child node of i""" 
    return 2*i + 1

def right(i):
    """Getter for the right child node of i"""
    return 2*i + 2

A = sys.stdin()
build_min_heap(A)
print(A)
sys.stdout(A)

#Stuff for testing
#A = [56,64,234,8,11224,6,0,356,234,54432,34,56,1234,578,356,25,-5, 0, -124, -356, 3346]
#B = []
#for i in range(200):
#    b = random.randint(-1000, 1000)
#    B.append(b)