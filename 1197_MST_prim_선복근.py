import sys

# inputs = []
# while True:
#     item = sys.stdin.readline().rstrip()
#     if item == '':
#         break
#     else:
#         inputs.append(item)

# count_nodes = inputs[0].split()[0]        
# count_edges = inputs[0].split()[1]   
# map = []     
# for item in inputs[1:]:
#     map.append(item.split())

# print(count_nodes)
# print(count_edges)
# print(map)

count_nodes = '3'
count_edges = '3'
map = {
    ('1', '2'): '1', 
    ('2', '3'): '2', 
    ('1', '3'): '3'
}

def Prim(G,r):
    '''집합 S를 공집합에서 시작해서 모든 정점(V)가 포함될 때까지 집합을 키워나감'''
    # 연결비용 초기화 : 초기정점(r=0), 나머지 정점(u=∞)
    S,V = set(),set()
    # 정점 r을 방문되었다고 표시하고, 집합 S에 포함시킨다
    # while S != V:
        # S에서 V-S를 연결하는 간선들 중 최소길이의 간선 (x,y)를 찾는다 (x는 방문한 정점, y는 방문하지 않은 정점) >>> (x ∈ S, y ∈ V-S)
        # 정점 y를 방문되었다고 표시하고, 집합 S에 포함시킨다
        # while 문이 한 번 반복되면 가장 짧은 하나의 정점이 S에 포함되는 구조


print(map[])