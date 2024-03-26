from itertools import permutations
import sys

# N = 4
N = int(sys.stdin.readline())

# cost = [
#     ['0', '10', '15', '20'],
#     ['5', '0', '9', '10'],
#     ['6', '13', '0', '12'],
#     ['8', '8', '9', '0'],
# ]
cost = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 도시 이름
cities = [i for i in range(N)]
print(cities)