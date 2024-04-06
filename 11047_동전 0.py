import sys
N,K = input().split()
N,K = int(N), int(K)
li = [int(sys.stdin.readline()) for _ in range(N)]

cnt = 0

def coin(K,li):
    global cnt
    while True:
        if K >= li[-1]:
            # print(K)
            # print(li)
            K = K - li[-1]
            cnt += 1
            if K == 0:
                break
        else:
            li.pop(-1)

    return cnt
print(coin(K,li))
# coin(K,li,cnt)