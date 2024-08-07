import sys

N, M = map(int, sys.stdin.readline().split())
# print(N,M)
names1 = set()
names2 = set()

for _ in range(N):
    names1.add(sys.stdin.readline().strip())

for _ in range(M):
    name = sys.stdin.readline().strip()
    if name in names1:
        names2.add(name)

# print(names1)
# print(names2)

sorted_names2 = sorted(names2)
print(len(sorted_names2))
for i in sorted_names2:
    print(i)