from collections import deque

def dfs(graph, start, visited):
    visited[start] = True
    print(start, end=' ')
    
    for neighbor in sorted(graph[start]):
        if not visited[neighbor]:
            dfs(graph, neighbor, visited)

def bfs(graph, start):
    visited = [False] * (N + 1)
    queue = deque([start])
    visited[start] = True
    
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        
        for neighbor in sorted(graph[v]):
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True

# 입력 받기
N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)]

# 그래프 구성
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# DFS 실행
visited = [False] * (N + 1)
dfs(graph, V, visited)
print()

# BFS 실행
bfs(graph, V)