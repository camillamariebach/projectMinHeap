import math

# find ud af hvordan man tager listen ind.

def min_heapify(A, i):
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

def extractMin(A): # Skal den tage A som argument? 
    min = A[0]
    A[0] = A[len(A)-1]
    min_heapify(A, 0) # skal det vaere nul her? 
    return min

def heap_min(A): 
    return A[0]

def insert(A, e):
    A.append(e)
    i = len(A)-1
    while i > 0 and A[parent(i)] > A[i]:
        temp = A[parent(i)]
        A[parent(i)] = A[i]
        A[i] = temp
        i = parent(i)


def build_min_heap(A): 
    m = math.floor((len(A)-1) / 2)
    for i in range(m, 0, -1): 
        min_heapify(A, i)

def heapsort(A):
    build_min_heap(A)
    end = len(A)-1
    for i in range(end, 1, -1): 
        temp = A[0]
        A[0] = A[i]
        A[i] = temp
        min_heapify(A, 0)

# Getters s. 152. Tage hoejde for manglende boern. 
def parent(i):
    return math.floor((i-1)/2)

def left(i):
    if i < len(A)-1: 
        return 2*i + 1

def right(i):
    if i < len(A)-1:
        return 2*i + 2


A = [2,7,24,6,7,3,2,6,8,9,56,432,64,234,8,11224,9,6,356,234,54432]

heapsort(A)
print(A)