N = int(input())
if N == 0:
    print(1)
else:
    res = 1
    while N > 1:
        res *= N
        N -= 1
    print(res)