import sys

def ks(N,K):
    if N == 0 or K == 0:
        return 0
    if K-W[N] < 0:
        dp[N][K] = dp[N-1][K]
    else:
        # print(dp[N-1][K-W[N]]+V[N])
        # print(dp[N-1][K])
        if ( ks(N-1,K-W[N]) + V[N] ) > ( ks(N-1,K) ):
            return ks(N-1,K-W[N]) + V[N]
        else:   
            return ks(N-1,K)


N,K = 4,7
# N,K = input().split()
# N,K = int(N), int(K)
W = [0,6,4,3,5]
V = [0,13,8,6,12]
dp = [[0 for _ in range(K+1)] for _ in range(N+1) ]
# W = [0]
# V = [0]


# li = [sys.stdin.readline().split() for _ in range(N)]
# for i in range(len(li)):
    # W.append(int(li[i][0]))
    # V.append(int(li[i][1]))

print(ks(N,K))