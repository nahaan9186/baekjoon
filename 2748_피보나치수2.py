def fibo(n):
    if n == 0:
        li[0] = 0
        # print(li[0])
        return li[0]
    if n == 1:
        li[1] = 1
        # print(li[1])
        return li[1]
    if not li[n-1]:
        li[n-1] = fibo(n-1)
        # print(li[n-1] + li[n-2])
        return li[n-1] + li[n-2]

N = int(input())
li = [0 for _ in range(N+1)]
# print(li)
print(fibo(N))