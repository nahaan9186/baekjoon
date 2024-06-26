a = input()
b = input()
n = len(a)
m = len(b)
dp = [[0 for i in range(m+1)] for j in range(n+1)]
def lcs(x, y):
    for i in range(1,n+1):
        for j in range(1,m+1):
            if x[i-1] == y[j-1]:
                dp[i][j] = dp[i-1][j-1]+1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[n][m]

print(lcs(a,b))