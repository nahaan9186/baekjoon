N,M = map(int, input().split())
# print(N,M)

li = [input().split() for _ in range(N)]
# print(li)

hash = {i[0]:i[1] for i in li}
# print(hash)


keys = [input() for _ in range(M)]
values = [hash[key] for key in keys]

for i in values:
    print(i)