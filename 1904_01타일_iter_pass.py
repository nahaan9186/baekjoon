import sys
sys.setrecursionlimit(500000)

def fibo(n):
    for _ in range(n+1): 
        if _ == 1:
            li[_] = 1
        elif _ == 2:
            li[_] = 2
        else:
            li[_] = (li[_-1] + li[_-2]) % 15746
    return li[_]

N = int(input())
li = [ 0 for _ in range(N+1)]
# print(li)
print(fibo(N))