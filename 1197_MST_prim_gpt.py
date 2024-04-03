import heapq

def prim(graph, start):
    visited = [False] * len(graph)  # graph의 길이만큼 visited list를 생성
    edges = [(0, start)]        # 맨 처음 시작할 vertex(root node)를 edges에 저장
    total_weight = 0
    while edges:        # edges(우선순위 큐)가 빌 때까지 반복
        weight, current_vertex = heapq.heappop(edges)       # edges에서 최소힙을 pop하고 unpack해서 각각 weight, current_vertex에 저장
        if not visited[current_vertex]:     # 방문한 적 없는 vertex에서만 실행
            visited[current_vertex] = True      # 방문기록을 True로 업데이트
            total_weight += weight      # 토탈 가중치 추가
            for next_vertex, weight in graph[current_vertex]:       # current_vertex를 1로 저장했기 때문에 자연스럽게 graph[current_vertex]는 다음 vertex를 가리키게 됨
                                                                    # 그러니까 첫 while문에서는 graph[1]을 언팩하게 되고, next_vertex는 2, weight는 1을 저장
                                                                    # 2번 vertex는 방문기록이 false이므로, 다음 if문을 실행 
                if not visited[next_vertex]:        # next_vertex 방문기록이 없는 경우만 실행
                    heapq.heappush(edges, (weight, next_vertex))        # 힙 구조를 유지하면서 우선순위 큐에 저장 (weight, next_vertex)
                                                                        # 첫 while문에서는 (1,2)를 저장
                                                                        # 두 번째 while문에서는 (3,3)을 저장
    return total_weight

V, E = map(int, input().split())
graph = [[] for _ in range(V + 1)]  # 인접 리스트 방식으로 graph를 생성, range를 V+1로 해서 정점 번호를 1부터 시작하게 맞춤

for _ in range(E):
    A, B, C = map(int, input().split())
    graph[A].append((B, C))     # A to B 경로의 가중치를 C로 저장, graph의 index가 출발점을 의미. 튜플의 0자리가 도착점, 1자리가 가중치
    graph[B].append((A, C))     # 양방향 그래프로 가정하고 B to A 경로의 가중치도 C로 저장

print(prim(graph, 1))  # 1번 정점에서 시작 