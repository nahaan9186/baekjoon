x = input()
res = 0

if x[0] == '0':
    if x[1] == 'x':
        i = 0
        j = -1
        lnth = len(x)
        while -j != lnth-1:
            if x[j] == 'a':
                res += 10 * (16**i)
            elif x[j] == 'b':
                res += 11 * (16**i)
            elif x[j] == 'c':
                res += 12 * (16**i)
            elif x[j] == 'd':
                res += 13 * (16**i)
            elif x[j] == 'e':
                res += 14 * (16**i)
            elif x[j] == 'f':
                res += 15 * (16**i)
            else:
                res += int(x[j]) * (16**i)
            i += 1
            j -= 1
    else:
        i = 0
        j = -1
        lnth = len(x)
        while -j != lnth:
            res += int(x[j]) * (8**i)
            i += 1
            j -= 1

else:
    res = int(x)

print(res)