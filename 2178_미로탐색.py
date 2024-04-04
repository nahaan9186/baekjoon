import sys  

N,M = 4,6

maze = [
    ('1','0','1','1','1','1'),
    ('1','0','1','0','1','0'),
    ('1','0','1','0','1','1'),
    ('1','1','1','0','1','1')
]

loc = [0,0]
set = {}
def escape(maze, N, M, loc, cnt=0):
    if maze[loc[0]][loc[1]] == 1:
        cnt += 1
        if (loc[0] == N & loc[1] == M):
            cnt += 1
            return cnt
        if maze[loc[0]+1][loc[1]] == 1:
            loc[0] += 1
            escape(maze, N, M, loc, cnt)
        if maze[loc[0]][loc[1]+1] == 1:
            loc[1] += 1
            escape(maze, N, M, loc, cnt)
    return cnt