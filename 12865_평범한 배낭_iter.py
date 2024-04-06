import sys

def ks(N,K):
    dp = [[0 for _ in range(K+1)] for _ in range(N+1) ]

    for c in range(1,K+1):
        for n in range(1,N+1):
            if c-W[n] < 0:
                dp[n][c] = dp[n-1][c]
            else:
                dp[n][c] = max( (dp[n-1][c-W[n]])+V[n], dp[n-1][c] )
    return dp[N][K]

N,K = input().split()
N,K = int(N), int(K)
W = [0]
V = [0]

li = [sys.stdin.readline().split() for _ in range(N)]
for i in range(len(li)):
    W.append(int(li[i][0]))
    V.append(int(li[i][1]))

print(ks(N,K))