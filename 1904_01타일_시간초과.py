import sys
sys.setrecursionlimit(1000000)

def setting(n):
    if n==1:
        li[1] = 1
    if n==2:
        li[1],li[2] = 1,2

def fibo(n):
    setting(n)
    if n == 1:
        return li[1]
    if n == 2: 
        return li[2]
    if li[n]==0:
        li[n] = fibo(n-2) + fibo(n-1)
        li[n] = li[n] % 15746
    # print(li)
    return li[n]
N = int(input())
li = [ 0 for _ in range(N+1)]


# print(li)
print(fibo(N))