n = int(input())
li = [input() for _ in range(n)]
# print(li)
q = []
for i in range(n):
    if li[i][:4] == 'push':
        a,b = li[i].split()
        q.append(int(b))
    if li[i] == 'front':
        if q == []:
            print(-1)
        else:
            print(q[0])
    if li[i] == 'back':
        if q == []:
            print(-1)
        else:
            print(q[-1])
    if li[i] == 'pop':
        if q == []:
            print(-1)
        else:
            print(q.pop(0))
    if li[i] == 'size':
        print(len(q))
    if li[i] == 'empty':
        if q == []:
            print(1)
        else:
            print(0)