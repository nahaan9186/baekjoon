import sys, random
from itertools import permutations

# 도시의 수
N = int(sys.stdin.readline())

# 도시 i에서 j로 가기 위한 비용
nested_list = [sys.stdin.readline().split() for i in range(N)] 
flattened_list = [item for sublist in nested_list for item in sublist]

# 모든 경로
def generate_coordinates(n):
    # 좌표 목록을 저장할 빈 리스트 생성
    coordinates = []
    
    # 0부터 n까지 x 좌표에 대해 반복
    for x in range(n):
        # 0부터 n까지 y 좌표에 대해 반복
        for y in range(n):
            # 현재 좌표 쌍을 리스트에 추가
            coordinates.append((x, y))
    
    # 생성된 좌표 목록 반환
    return coordinates

route = generate_coordinates(N)

def create_dict(a:list,b:list) -> dict:
    dic = {}
    for i in range(len(b)):
        dic[a[i]] = b[i] 
    return(dic)

mapping = create_dict(route,flattened_list)

def find_route(dic:any, base_city:int) -> int:
    ground = [i for i in range(N)]
    ground.remove(base_city)
    total_cost = 0
    next = random.choice(ground)
    total_cost += int(dic[(base_city, next)])
    ground.remove(next)
    while ground != []:
        next2 = random.choice(ground)
        while True:
            if next != next2:
                break
        total_cost += int(dic[(next, next2)])
        ground.remove(next2)
        next,next2 = next2,next
    total_cost += int(dic[(next , base_city)])

    return total_cost

res = 99999999
for k in range(100000):
    for j in range(N):
        total_cost = find_route(mapping, j)
        if total_cost < res:
            res = total_cost


print(res)