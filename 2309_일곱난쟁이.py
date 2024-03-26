import sys, random

li = [int(sys.stdin.readline()) for i in range(9)] 

def sampling(A):
    S = []
    S = random.sample(A,7)
    if sum(S) == 100:
        S.sort()
        for i in range(7):
            print(S[i])
    else:
        sampling(A) 

sampling(li)