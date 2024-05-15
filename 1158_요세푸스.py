n, k = map(int, input().split())

li = list(range(1,n+1))
# print(li)
res = []

idx = k-1
while (li != []):
    length = len(li)
    # print(idx, length)
    while idx >= length:
        idx -= length
    res.append(li.pop(idx))
    idx += k-1
    
print('<' + ', '.join(map(str, res)) + '>')
