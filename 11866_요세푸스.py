import sys
from collections import deque

a = sys.stdin.readline().strip().split()
N, K = int(a[0]), int(a[1])

dq = deque(range(1,N+1)) # range로 덱의 최대길이를 제한
res = []
while dq:
    # K-1번째 요소들을 뒤로 이동
    dq.rotate(-(K-1))
    # K번째 요소 제거 및 결과 리스트에 추가
    res.append(dq.popleft())

str = '<'
for i in res:
    if i != res[-1]:
        str += f'{i}, '
    else:
        str += f'{i}'
str += '>'
print(str)