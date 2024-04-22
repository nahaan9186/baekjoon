
n = int(input())
li = []
for _ in range(n):
    li.append(input())

for _ in range(n):
    print(int(li[_][0]) + int(li[_][2]))