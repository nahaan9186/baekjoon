from itertools import permutations
import sys


# 도시의 수
# N = 4 
N = int(sys.stdin.readline())

# 도시 i에서 j로 가기 위한 비용
cost = [sys.stdin.readline().split() for i in range(N)] 
# cost = [
#     ['0','10','15','20'],
#     ['5','0','9','10'],
#     ['6','13','0','12'],
#     ['8','8','9','0'],
# ]   

# 도시 이름
cities = [ i for i in range(N) ]
perms = list(permutations(cities))
perms_2 = []

for perm in perms:
    perm = list(perm)
    perm.append(perm[0])
    perms_2.append(perm)   

tots = []
for j in range(len(perms_2)):
    tot = 0
    if perms_2[j].count('0') >= 2:
        continue
    for i in range(N): 
        tot += int(cost[perms_2[j][i]][perms_2[j][i+1]])
    tots.append(tot)
res = min(tots)
 
print(res)