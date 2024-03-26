import sys  
a = [int(sys.stdin.readline()) for i in range(9)]  #첫째 줄부터 아홉 번째 줄까지 한 줄에 하나의 자연수
cnt = 1
res = a[0]

for i in range(len(a)):
    if (i > 0) & (a[i] > res) & (i < 10):
        res = a[i] 
        cnt = i+1

print(res)
print(cnt)