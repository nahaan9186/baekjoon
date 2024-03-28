import sys
import heapq

N = int(sys.stdin.readline().strip())
li_N = [int(sys.stdin.readline().strip()) for i in range(N)]

A = []
for i in li_N:
    if i == 0:
        if not A:
            print(0)
        else:
            print(-heapq.heappop(A))
    else:
        heapq.heappush(A,-i)