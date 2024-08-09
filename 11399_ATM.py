
N = int(input())
P = input().split()
P = [int(x) for x in P]
P.sort()

for i in range(N-1):
    P[i+1] = P[i+1] + P[i]

print(sum(P))