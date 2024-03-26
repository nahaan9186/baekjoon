import sys
from wsgiref.handlers import IISCGIHandler  

T = int(input())
case = []
for i in range(T):
    case.append(list(sys.stdin.readline().split()))
#case 의 모양은 [['1', 'sdf'], ['2', 'sdf'], ['3', 'sdf']]

for ii in range(len(case)):
    res = []
    for iii in range(len(case[ii][1])):
        res.append(case[ii][1][iii] * int(case[ii][0]))
    res = ''.join(str(number) for number in res)
    print(res)



