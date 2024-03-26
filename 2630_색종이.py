import sys  
from copy import deepcopy


N = int(sys.stdin.readline())
# N = 8
# paper = [
#     ['1','1','0','0','0','0','1','1'],
#     ['1','1','0','0','0','0','1','1'],
#     ['0','0','0','0','1','1','0','0'],
#     ['0','0','0','0','1','1','0','0'],
#     ['1','0','0','0','1','1','1','1'],
#     ['0','1','0','0','1','1','1','1'],
#     ['0','0','1','1','1','1','1','1'],
#     ['0','0','1','1','1','1','1','1']
# ]

paper = [sys.stdin.readline().split() for i in range(N)] 

def comp(x:str,y:any) -> bool:
    return all(x == element for sublist in y for element in sublist)

def quarter(paper:any) -> None:
    global cnt_w, cnt_b 

    if comp(paper[0][0], paper) == False:
        part1 = deepcopy(paper[:len(paper) // 2])    
        for j in range(len(paper) // 2):
            for k in range(len(paper) // 2):
                part1[j].pop()
        if comp(part1[0][0], part1) == True:
            if part1[0][0] == '0':
                cnt_w += 1
            else:
                cnt_b += 1
        else:
            quarter(part1)

        part2 = deepcopy(paper[:len(paper) // 2])   
        for j in range(len(paper) // 2):
            for k in range(len(paper) // 2):
                part2[j].pop(0)
        if comp(part2[0][0], part2) == True:
            if part2[0][0] == '0':
                cnt_w += 1
            else:
                cnt_b += 1
        else:
            quarter(part2)

        part3 = deepcopy(paper[len(paper) // 2:])    
        for j in range(len(paper) // 2):
            for k in range(len(paper) // 2):
                part3[j].pop()
        if comp(part3[0][0], part3) == True:
            if part3[0][0] == '0':
                cnt_w += 1
            else:
                cnt_b += 1
        else:
            quarter(part3)

        part4 = deepcopy(paper[len(paper) // 2:])   
        for j in range(len(paper) // 2):
            for k in range(len(paper) // 2):
                part4[j].pop(0)
        if comp(part4[0][0], part4) == True:
            if part4[0][0] == '0':
                cnt_w += 1
            else:
                cnt_b += 1
        else:
            quarter(part4)
    else:
        if paper[0][0] == '0':
            cnt_w += 1
        else:
            cnt_b += 1
    
cnt_w = 0
cnt_b = 0

def res() -> None:   
    quarter(paper)
    print(cnt_w)
    print(cnt_b)

res()