N = 4   # number of item
K = 7   # capacity
W = [6,4,3,5]   # weight
V = [13,8,6,12] # value

def knapsack(values, weights, capacity):
    dp = [[0 for _ in range(capacity + 1)] for _ in range(N + 1)]

    for i in range(1, N + 1):       
    # 모든 아이템 순회, dp[0][x]는 모든 x에 대해 0으로 초기화되어 있으므로, 아이템이 0개인 경우를 나타냄
        for w in range(1, capacity + 1):    
        # 각 아이템 i에 대해, 모든 가능한 용량 w를 1부터 capacity까지 순회하면서 현재 아이템과 용량으로 달성할 수 있는 최대 가치를 계산
            if weights[i-1] <= w:
            # 현재 아이템 i가 현재 용량 w를 초과하지 않고 배낭에 추가될 수 있는지 확인
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-weights[i-1]] + values[i-1])
                # 현재 아이템을 포함하지 않고 달성할 수 있는 최대 가치와
                # 현재 아이템을 포함하고 현재 아이템의 가치를 추가한 후 남은 용량으로 달성할 수 있는 최대 가치
            else:
                dp[i][w] = dp[i-1][w]
                # 현재 아이템을 추가하면 용량을 초과하는 경우
                # 현재 아이템을 고려하지 않는 것과 같은 값을 dp[i][w]에 설정하여 사실상 현재 아이템을 제외
    return dp[N][capacity]

print(knapsack(V,W,K))