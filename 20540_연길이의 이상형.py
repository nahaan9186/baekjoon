MBTI = input()

if MBTI[0] == 'E':
    res = 'I'
else:
    res = 'E'

if MBTI[1] == 'S':
    res = res + 'N'
else:
    res = res + 'S'
    
if MBTI[2] == 'T':
    res = res + 'F'
else:
    res = res + 'T'

if MBTI[3] == 'J':
    res = res + 'P'
else:
    res = res + 'J'

print(res)