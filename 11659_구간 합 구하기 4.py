N, M = map(int, input().split())
nums = list(map(int, input().split()))

# 누적 합 배열 생성
prefix_sums = [0] * (N + 1)
for idx in range(1, N + 1):
    prefix_sums[idx] = prefix_sums[idx - 1] + nums[idx - 1]

res_li = []

# 구간 합을 O(1)로 계산
for _ in range(M):
    i, j = map(int, input().split())
    res = prefix_sums[j] - prefix_sums[i - 1]
    res_li.append(res)

for res in res_li:
    print(res)
