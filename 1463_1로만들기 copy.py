dp_list = [0] * 1000001  # 연산 횟수를 저장할 리스트 초기화

def findMin(X):
    for i in range(2, X + 1):
        # 기본적으로 1을 빼는 연산
        dp_list[i] = dp_list[i - 1] + 1
        
        # 2로 나누어 떨어지는 경우
        if i % 2 == 0:
            dp_list[i] = min(dp_list[i], dp_list[i // 2] + 1)
        
        # 3으로 나누어 떨어지는 경우
        if i % 3 == 0:
            dp_list[i] = min(dp_list[i], dp_list[i // 3] + 1)

    return dp_list[X]

N = int(input())
print(findMin(N))
