n = int(input())

def set_farm():
    x,y,z = map(int,input().split())
    lettuce = [ [0 for _ in range(x+2)] for _ in range(y+2) ]

    while z > 0:
        a,b = map(int,input().split())
        lettuce[b+1][a+1] = 1
        z -= 1

    return lettuce

li = []
while n > 0:
    li.append(set_farm())
    n -= 1

# for i in range(len(li)):
#     for j in range(len(li[i])):
#         print(li[i][j])

res = []
for i in range(len(li)):
    cnt = 0
    let = li[i]
    for j in range(1,len(let)-1):
        for k in range(1,len(let[j])-1):
            if let[j][k] == 1:
                if let[j-1][k] == 0 and let[j][k-1] == 0:
                    cnt += 1
                    if (let[j+1][k] == 1):
                        cnt -= 1
                    continue
                if (let[j-1][k] == 1):
                    continue
                if (let[j][k-1] == 1):
                    continue
                cnt += 1
            # print(j, k, cnt)
    res.append(cnt)
    # print(let)

# print()
# for i in range(len(li)):
#     for j in range(len(li[i])):
#         print(li[i][j])

for i in range(len(res)):
    print(res[i])