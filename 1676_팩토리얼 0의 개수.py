import sys
sys.setrecursionlimit(1000000)

def fac(n):
    if n == 1:
        return n
    return n * fac(n-1)

def sol():
    n = int(input())
    if n == 0:
        return 0
    s = str(fac(n))
    # print(s[-1])
    cnt = 0
    i = -1
    while s[i] == '0':
        # print(s[i])
        cnt += 1
        i -= 1
    return cnt

print(sol())