import heapq

def dijkstra(start, end, graph, N):
    INF = float('inf')
    dist = [INF] * (N + 1)
    dist[start] = 0
    queue = []
    heapq.heappush(queue, (0, start))
    
    while queue:
        current_dist, current_node = heapq.heappop(queue)
        
        if dist[current_node] < current_dist:
            continue
            
        for adj, w in graph[current_node]:
            distance = current_dist + w
            if distance < dist[adj]:
                dist[adj] = distance
                heapq.heappush(queue, (distance, adj))
                
    return dist[end]

N = int(input())  # 도시의 개수
M = int(input())  # 버스의 개수
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

start, end = map(int, input().split())

print(dijkstra(start, end, graph, N))
