li = []
while True:
    li.append(input())
    if li[-1] == '0 0':
        break

# print(li)

for i in li:
    tmp = i.split()
    if tmp[0] == '0' or tmp[1] == '0':
        print('AXIS')
        continue
    if tmp[0][0] == '-' or tmp[1][0] == '-':
        if tmp[0][0] == '-' and tmp[1][0] == '-':
            print('Q3')
            continue
        if tmp[0][0] == '-' and tmp[1][0] != '-':
            print('Q2')
            continue
        if tmp[0][0] != '-' or tmp[1][0] == '-':
            print('Q4')
            continue
    else:
        print('Q1')
