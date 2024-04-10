import sys

li = sys.stdin.readline().split()
n, k = li
n, k = int(n), int(k)
li_2 = [sys.stdin.readline().strip() for _ in range(n)]
for i in range(n):
    li_2[i] = int(li_2[i])
li_2.sort()

dp = [[]]

def coin(k, li_2, cnt=-1):
    if k == 0:
        return cnt
    if k < li_2[-1]:
        return coin(k, li_2[:-1], cnt)
    if k >= li_2[-1]:
        if cnt == -1:
            cnt = 0
        return coin(k - li_2[-1], li_2, cnt + 1)

print(coin(k, li_2))

