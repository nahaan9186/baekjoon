def bag_count(N):
    if N < 5:
        if N % 3 == 0:
            return 1
        else:
            return -1
    if N == 5:
        return 1
    a = N // 5
    while a >= 0:
        b = N - ( 5 * a )
        if b % 3 == 0:
            return a+(b//3)
        a -= 1
    else:
        return -1

N = int(input())

print(bag_count(N))