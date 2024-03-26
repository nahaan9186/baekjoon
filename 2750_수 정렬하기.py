import sys

N = int(sys.stdin.readline())
li = [int(sys.stdin.readline()) for i in range(N)] 

def quickSort( A:list, L:int, R:int ):
    if L < R:
        pivot = partition(A,L,R)
        quickSort(A,L,pivot -1)
        quickSort(A,pivot +1, R)
    return A

def partition(A:list, x:int, y:int) -> int:
    i = x - 1
    j = x
    while j < y :
        if A[j] <= A[y]:
            i += 1
            A[i],A[j] = A[j],A[i]
        j += 1
    A[i+1],A[y] = A[y],A[i+1]
    return i+1

res = quickSort(li, 0, len(li)-1)
for i in res:
    print(i)