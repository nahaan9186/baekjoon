def max_score(stairs):
    n = len(stairs)
    if n <= 2:
        return sum(stairs)
    
    dp = [0] * n
    dp[0] = stairs[0]
    dp[1] = stairs[0] + stairs[1]
    
    for i in range(2, n):
        dp[i] = max(
                    dp[i-2] + stairs[i],
                    dp[i-3] + stairs[i-1] + stairs[i]
                    )
    
    return dp[-1]

# 입력 받기
n = int(input())
stairs = [int(input()) for _ in range(n)]

# 결과 출력
print(max_score(stairs))