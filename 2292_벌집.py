n = int(input())

cnt = 1
n -= 1

while n // 6*cnt >= 0 :
    if n == 0:
        break
    # print(n,cnt)
    n -= 6*cnt
    cnt += 1
    
print(cnt)

    

