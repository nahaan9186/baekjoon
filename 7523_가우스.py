n = int(input())

li = [input() for _ in range(n)]

for i, item in enumerate(li):
    tmp = item.split()
    a, b = int(tmp[0]), int(tmp[1])
    var = (a+b) // 2
    cnt = (b-a+1) // 2
    isodd = (b-a+1) % 2 
    if isodd == 1:
        res = (a+b) * cnt
        res += var
    else:
        res = (a+b) * cnt
    print(f'Scenario #{i+1}:')
    print(res)
    if item == li[-1]:
        break
    print()