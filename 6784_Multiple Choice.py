n = int(input())

ans = [input() for i in range(n)]
sub = [input() for i in range(n)]

score = 0
for i in range(n):
    if ans[i] == sub[i]:
        score += 1

print(score)