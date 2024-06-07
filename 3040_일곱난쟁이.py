import random

li = []
for i in range(9):
    li.append(int(input()))

while True:
    res = []
    for i in li:
        res.append(i)
    idx1 = random.randint(0,8)
    res.pop(idx1)
    idx2 = random.randint(0,7)
    res.pop(idx2)
    if sum(res) == 100:
        break

for i in res:
    print(i)
    