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

for i in range(len(li)):
    for j in range(len(li[i])):
        print(li[i][j])

cnt = 0
def search(let, i, j, k, l):
    if i == k and j == l:
        return 0
    global cnt
    cnt += 1
    if let[i+1][j] == 1:
        let[i][j] += 1
        search(let, i+1, j, k, l)
    if let[i][j+1] == 1:
        let[i][j] += 1
        search(let, i, j+1, k, l)
    if let[i-1][j] == 1:
        let[i][j] += 1
        search(let, i-1, j, k, l)
    if let[i][j-1] == 1:
        let[i][j] += 1
        search(let, i, j-1, k, l)

for i in range(len(li)):
    cnt = 0
    let = li[i]
    for j in range(1,len(let)):
        for k in range(1,len(let[j])):
            if let[j][k] == 1:
                cnt += 1
                search(let,)


# print()
# for i in range(len(li)):
#     for j in range(len(li[i])):
#         print(li[i][j])

# for i in range(len(res)):
#     print(res[i])