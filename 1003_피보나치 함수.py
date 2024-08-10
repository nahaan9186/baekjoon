dp_list = [[] for _ in range(41)]
dp_list[0] = [1,0]
dp_list[1] = [0,1]
dp_list[2] = [1,1]
# print(dp_list)

for i in range(3,41):
    dp_list[i] = [dp_list[i-1][0] + dp_list[i-2][0] , dp_list[i-1][1] + dp_list[i-2][1]]
    
# print(dp_list)

T = int(input())
N = [int(input()) for _ in range(T)]
for i in N:
    res = dp_list[i]
    print(f"{res[0]} {res[1]}")