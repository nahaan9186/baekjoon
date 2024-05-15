n = int(input())
li = [input() for _ in range(n)]
# print(li)
q = []
for i in range(n):
    if li[i][:9] == 'push_back':
        a,b = li[i].split()
        q.append(int(b))
    if li[i][:10] == 'push_front':
        a,b = li[i].split()
        q.insert(0,int(b))
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
    if li[i] == 'pop_front':
        if q == []:
            print(-1)
        else:
            print(q.pop(0))
    if li[i] == 'pop_back':
        if q == []:
            print(-1)
        else:
            print(q.pop(-1))
    if li[i] == 'size':
        print(len(q))
    if li[i] == 'empty':
        if q == []:
            print(1)
        else:
            print(0)