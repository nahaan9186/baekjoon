
n = int(input())
li = [input().strip() for _ in range(n)]
for i in range(n):
    li[i] = int(li[i])
    
# print(li)

avg = round( sum(li) / len(li) )

print(avg)

li.sort()
mid = li[ len(li) // 2 ]

print(mid)

# mpv

    
e=[]
d={}
for i in li:
    d[i]=1
for i in li:
    d[i]+=1
for key,values in d.items():
    if values==max(d.values()):
        e.append(key) 
    else:
        pass 
# e.sort()
if len(e) > 1:
    print(e[1])  
else:
    print(e[0])

rng = max(li) - min(li)

print(rng)