class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))    # 각 요소의 부모를 나타내는 배열을 초기화
                                        # 초기에는 각 요소가 자신만을 포함하는 집합의 대표로 설정되므로, 각 요소의 부모는 자기 자신
        self.rank = [0] * n             # 트리의 깊이(높이)를 추정하는 데 사용
                                        # 트리를 합칠 때 더 낮은 깊이의 트리를 더 높은 깊이의 트리 아래에 붙이는 방식으로 사용
                                        # 트리의 높이를 가능한 낮게 유지하여 'find'연산의 효율을 높이는 데 도움을 준다
    def find(self, u):
        if u != self.parent[u]:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u] 

    def union(self, u, v):
        root1 = self.find(u)                    # u의 부모를 찾아 root1에 저장
        root2 = self.find(v)                    # v의 부모를 찾아 root2에 저장
        if root1 != root2:                      # 둘이 서로 다르면 
            if self.rank[root1] > self.rank[root2]:         # rank(degree)를 비교
                self.parent[root2] = root1                  # root1이 더 깊으면 root2의 부모를 root1으로 변경 
            else:
                self.parent[root1] = root2
                if self.rank[root1] == self.rank[root2]:    # 두 트리의 rank가 같을 떄, 한 트리를 다른 트리 아래에 붙임
                    self.rank[root2] += 1                   # 그리고 합쳐진 트리의 rank를 1증가

def kruskal(V, edges):
    mst = []
    edges.sort(key=lambda x: x[2])  # 각 간선을 나타내는 튜플'x'를 입력받아 x[2]를 반환(가중치 반환)
                                    # 즉, 각 간선을 그 간선의 가중치에 따라 정렬
    disjoint_set = DisjointSet(V + 1)   # 'V + 1'을 파라미터로 사용하는 이유는 대부분의 그래프 문제에서 정점(vertex)의 번호가 1부터 시작한다는 관례 때문
                                        # 이렇게 하면 정점 번호와 배열의 인덱스가 일치하게 되어, 0번 인덱스를 사용하지 않고 1번 인덱스부터 V번 인덱스까지 사용
    mst_weight = 0
    for u, v, weight in edges:          # 앞서 edges에 저장한 튜플들을 각각 u,v,weight 변수에 unpacking
        if disjoint_set.find(u) != disjoint_set.find(v):    # u와 v의 부모를 탐색
            disjoint_set.union(u, v)                        # 부모가 다르면 union
            mst.append((u, v))
            mst_weight += weight

    return mst_weight

V, E = map(int, input().split())
edges = []
for _ in range(E):
    A, B, C = map(int, input().split())
    edges.append((A, B, C))

print(kruskal(V, edges))