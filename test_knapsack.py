def knapsack(values, weights, capacity):
    n = len(values)
    # item의 갯수
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    # 2차원 배열 초기화하여 dp에 저장
    # 각 셀 dp[i][w]는 첫 번째 i개 아이템과 배낭 용량 w를 가질 때 달성할 수 있는 최대 가치
    # 어떤 아이템도 선택되지 않았거나 용량이 0인 경우를 포함하기 위해 n+1과 capacity+1을 사용

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-weights[i-1]] + values[i-1])
            else:
                dp[i][w] = dp[i-1][w]

    return dp[n][capacity]

# Example usage
values = [60, 100, 120]  # The values of the items
weights = [10, 20, 30]   # The weights of the items
capacity = 50            # Maximum capacity of the knapsack
print(knapsack(values, weights, capacity))