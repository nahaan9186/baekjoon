a = input()
b = input()
n = len(a)
m = len(b)
dp = [[0 for i in range(m+1)] for j in range(n+1)]
def lcs(x, y):
    # 바닥조건
    if not x and not y:
        return 0
    if (not x or not y) or (x[-1] != y[-1]):
        if not x:
            dp[n][m] = lcs(x, y[:-1])
        elif not y:
            dp[n][m] = lcs(x[:-1], y)
        else:
            dp[n][m] = max(lcs(x[:-1], y), lcs(x, y[:-1]))
    else:
        dp[n][m] = lcs(x[:-1], y[:-1]) + 1


lcs(a, b)
print(dp[n][m])