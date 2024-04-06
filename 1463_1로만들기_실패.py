def divide(N):
    cnt = 0
    while N != 1:
        if N % 3 == 0:
            N = N // 3
            cnt += 1
        elif (N % 2 == 0) and ((N-1)%3 != 0) and ((N-2)%3 != 0):
            N = N // 2
            cnt += 1
        else:
            N = N-1
            cnt += 1
    return cnt

N = int(input())
print(divide(N))