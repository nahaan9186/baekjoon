import sys

N = int(sys.stdin.readline())
paper = [sys.stdin.readline().split() for _ in range(N)]
li = [0,0,0]

def judge(paper):
    flag = 1
    L = len(paper[0])
    if L == 1:
        count(paper)
        return 0
    for i in range(L):
        for j in range(L):
            if paper[i][j] != paper[0][0]:
                flag = 0
                break
        if flag == 0:
            break

    if flag == 0:
        split(paper)
    
    if flag == 1:
        count(paper)
    
    return flag

def split(paper):
    p1,p2,p3,p4,p5,p6,p7,p8,p9 = [],[],[],[],[],[],[],[],[]
    th = len(paper[0])//3
    for i in range(th):
        p1.append(paper[i][:th])
        p2.append(paper[i][th:th*2])
        p3.append(paper[i][th*2:])
    for i in range(th):
        p4.append(paper[i+th][:th])
        p5.append(paper[i+th][th:th*2])
        p6.append(paper[i+th][th*2:])
    for i in range(th):
        p7.append(paper[i+th*2][:th])
        p8.append(paper[i+th*2][th:th*2])
        p9.append(paper[i+th*2][th*2:])
    judge(p1)
    judge(p2)
    judge(p3)
    judge(p4)
    judge(p5)
    judge(p6)
    judge(p7)
    judge(p8)
    judge(p9)

def count(paper):
    if paper[0][0] == '-1':
        li[0] += 1
        return li
    if paper[0][0] == '0':
        li[1] += 1
        return li
    if paper[0][0] == '1':
        li[2] += 1
        return li

judge(paper)

a,b,c = li
print(a)
print(b)
print(c)