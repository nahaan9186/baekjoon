import sys

def slice(line):
    if len(line) == 0:
        return '-'
    if len(line) == 1:
        return line
    return erase(line)

def erase(line):
    if len(line) == 0:
        return '-'
    if len(line) == 1:
        return line
    i = len(line) // 3
    new_line = erase(line[:i]) + ' '*i + erase(line[i*2:])
    return new_line

li = []
while True:
    num = sys.stdin.readline().rstrip()
    if num == '':
        break
    else:
        li.append(int(num))
        
for _ in li:
    line = '-'*(3**int(_))
    print(slice(line))