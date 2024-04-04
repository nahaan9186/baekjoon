N,M,V = 4,5,1
edges = [(1,2),(1,3),(1,4),(2,4),(3,4)]
edges.sort()
degree = edges[-1][0] - edges[0][0] + 1

def graph(edges, degree):
    graph = [[] for _ in range(degree + 1)]
    while edges:
        node = edges.pop(0)
        graph[node[0]].append(node)
    return graph

def bfs(start, graph):
    '''bfs는 큐'''
    queue, visited = [],[]
    for line in graph[start:]:
        for item in line:
            a, b = item
            if a not in visited:
                queue.append(a)
                visited.append(a)
            if b not in visited:
                queue.append(b)
                visited.append(b)
    return queue

def dfs(start, graph, stack, visited):
    '''dfs는 스택'''
    if visited == None: 
        stack, visited = [],set()
        stack.append(start)
        visited.add(start)
    while len(visited) < N:
        if graph[start][0][1] not in visited:
            next_one = graph[start][0][1]
            stack.append(next_one)
            visited.add(next_one)
            stack = dfs(next_one, graph, stack ,visited)
    return stack    

graphy = graph(edges,degree)
# print(bfs(V, graphy))
print(dfs(V, graphy, None, None))