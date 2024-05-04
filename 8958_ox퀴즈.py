n = int(input())
li = [input() for _ in range(n)]
sum = [0 for _ in range(n)]

for i in range(len(li)):
    score = 0
    for j in range(len(li[i])):
        if li[i][j] == 'X':
            score = 0
            continue
        if li[i][j] == 'O':
            score = score + 1
            # print(score)
            sum[i] += score
        # print(sum)
    
for i in sum:        
    print(i)