class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            elif self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1

def kruskal(nodes, edges):
    uf = UnionFind(nodes)
    mst_weight = 0

    # 간선을 가중치에 따라 정렬
    sorted_edges = sorted(edges, key=lambda x: x[2])

    for u, v, weight in sorted_edges:
        # 사이클이 형성되지 않는 경우, 간선을 선택
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst_weight += weight
    return mst_weight

# 입력 데이터 처리
count_nodes, count_edges = map(int, inputs[0].split())
edges = [list(map(int, x.split())) for x in inputs[1:]]

# 크루스칼 알고리즘을 사용하여 MST의 가중치 계산
print(kruskal(count_nodes, edges))
