
def dfs(graph, start, visited):
    visited[start] = True
    # print(start, end=' ')
    global res
    if start != 1 & start != None:
        res += 1
    
    for neighbor in sorted(graph[start]):
        if not visited[neighbor]:
            dfs(graph, neighbor, visited)

# 입력 받기
N = int(input())    # 컴퓨터의 수
M = int(input())    # 연결되어 있는 컴퓨터 쌍의 수
graph = [[] for _ in range(N + 1)]  # 그래프 초기화
res = 0

# 그래프 구성
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)            

visited = [False] * (N + 1)

dfs(graph,1,visited)
print(res)