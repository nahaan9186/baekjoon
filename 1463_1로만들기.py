dp_list = [ -1 for i in range(10001)]
# print(dp_list)
# print(dp_list[0][0])

def findMin(X, y):
    if dp_list[X] != -1:  # 이미 계산된 값이 있으면 그 값을 반환
        return dp_list[X]
    if X == 1:  # 기본 케이스
        return y
    y += 1
    if (X % 3 == 0) & (X % 2 == 0):
        dp_list[X] = min(findMin(X // 3, y),
                         findMin(X // 2, y),
                         findMin(X - 1, y))
    elif (X % 3 == 0) & (X % 2 != 0):
        dp_list[X] = min(findMin(X // 3, y),
                         findMin(X - 1, y))
    elif (X % 3 != 0) & (X % 2 == 0):
        dp_list[X] = min(findMin(X // 2, y),
                         findMin(X - 1, y))
    else:
        dp_list[X] = findMin(X - 1, y)
    
    return dp_list[X]  # 계산된 값을 반환
    
# for i in range(1,101):
#     dp_list[i] = findMin(i,0)

N = int(input())
print(findMin(N,0))
    