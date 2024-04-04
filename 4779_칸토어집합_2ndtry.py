def slice(line):
    if len(line) == 1:
        return line
    
def replace(line):
    th = len(line) // 3
    

N = int(input())
line = ['-' for _ in range(3**N)]
