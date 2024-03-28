import sys
from collections import deque

N = int(sys.stdin.readline().strip())
li_N = [sys.stdin.readline().split() for i in range(N)]

# print(f'=============================================================================')
# print(N)
# print(li_N)

d = deque()
for i in li_N:
    if i[0] == 'push':
        d.append(i[1])
    if i[0] == 'top':
        if not d:
            print(-1)
        else:
            print(d[-1])
    if i[0] == 'size':
        print(len(d))
    if i[0] == 'pop':
        if not d:
            print(-1)
        else:
            print(d.pop())
    if i[0] == 'empty':
        print(1 if not d else 0)
