li = []
i = 0
while True:
    li.append([])
    a, b, c = input().split()
    a, b, c = int(a), int(b), int(c)

    if a + b + c == 0:
        break

    li[i].append(a)
    li[i].append(b)
    li[i].append(c)
    i += 1

# print(li)
res = []
for i in range(len(li)-1):
    # print(li[i])
    if li[i][0]**2 + li[i][1]**2 == li[i][2]**2:
        res.append('right')
    elif li[i][1]**2 + li[i][2]**2 == li[i][0]**2:
        res.append('right')
    elif li[i][2]**2 + li[i][0]**2 == li[i][1]**2:
        res.append('right')
    else:
        res.append('wrong')

for item in res:
    print(item)