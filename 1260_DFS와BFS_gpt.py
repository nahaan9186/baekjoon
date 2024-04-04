N, M, V = 4, 5, 1
edges = [(1, 2), (1, 3), (1, 4), (2, 4), (3, 4)]
edges.sort()
degree = edges[-1][0] - edges[0][0] + 1

def graph(edges, degree):
    graph = [[] for _ in range(degree + 1)]
    for edge in edges:
        graph[edge[0]].append(edge[1])  # Assuming directed edge for simplicity
        graph[edge[1]].append(edge[0])  # Add this line if your graph is undirected
    return graph

def bfs(start, graph):
    '''BFS uses a queue'''
    queue, visited = [start], set([start])
    result = []

    while queue:
        node = queue.pop(0)
        result.append(node)
        for adj in graph[node]:
            if adj not in visited:
                queue.append(adj)
                visited.add(adj)
    return result

def dfs(start, graph, visited=None):
    '''DFS uses a stack'''
    if visited is None:
        visited = set()
    visited.add(start)
    result = [start]

    for adj in graph[start]:
        if adj not in visited:
            result.extend(dfs(adj, graph, visited))
    return result

# Adjusting the graph creation function to properly build an adjacency list
graphy = graph(edges, degree)
bfs_result = bfs(V, graphy)
dfs_result = dfs(V, graphy)

print("BFS:", bfs_result)
print("DFS:", dfs_result)

