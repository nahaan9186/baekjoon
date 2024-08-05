# 첫째 줄에 수행해야 하는 연산의 수 M (1 ≤ M ≤ 3,000,000)이 주어진다.
# 둘째 줄부터 M개의 줄에 수행해야 하는 연산이 한 줄에 하나씩 주어진다.

# add x: S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.
# remove x: S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.
# check x: S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)
# toggle x: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)
# all: S를 {1, 2, ..., 20} 으로 바꾼다.
# empty: S를 공집합으로 바꾼다.

##################### 내가 짠 코드 = 메모리 초과
# M = int(input())
# li = [input().split() for _ in range(M)]
# S = set()

# for i in li:
#     if i[0] == 'add':
#         S.add(int(i[1]))
#     if i[0] == 'remove':
#         S.discard(int(i[1]))
#     if i[0] == 'check':
#         if int(i[1]) in S:
#             print(1)
#         else:
#             print(0)
#     if i[0] == 'toggle':
#         if int(i[1]) in S:
#             S.discard(int(i[1]))
#         else:
#             S.add(int(i[1]))
#     if i[0] == 'all':
#         S = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}
#     if i[0] == 'empty':
#         S.clear()
##################### 내가 짠 코드 = 메모리 초과
    
import sys

M = int(sys.stdin.readline())
S = set()

for _ in range(M):
    command = sys.stdin.readline().split()
    
    if command[0] == 'add':
        S.add(int(command[1]))
    elif command[0] == 'remove':
        S.discard(int(command[1]))
    elif command[0] == 'check':
        print(1 if int(command[1]) in S else 0)
    elif command[0] == 'toggle':
        if int(command[1]) in S:
            S.discard(int(command[1]))
        else:
            S.add(int(command[1]))
    elif command[0] == 'all':
        S = set(range(1, 21))
    elif command[0] == 'empty':
        S.clear()