import sys
sys.setrecursionlimit(10**7)
Z = sys.stdin.readline().split()

n, r, c = Z
n, r, c = int(n), int(r)-1, int(c)-1

ZMAP = [[0 for i in range(2**n)] for i in range(2**n)]
cnt = -1

def split(zmap):
    global cnt, i, j
    zmap1, zmap2, zmap3, zmap4 = [],[],[],[]
    L = len(zmap[0])//2
    if len(zmap[0]) == 2:
        cnt += count(zmap)
    else:
        zmap1 = [zmap[_][:L] for _ in range(L)]
        split(zmap1)
        zmap2 = [zmap[_][L:] for _ in range(L)]
        split(zmap2)
        zmap3 = [zmap[_+L][:L] for _ in range(L)]
        split(zmap3)
        zmap4 = [zmap[_+L][L:] for _ in range(L)]
        split(zmap4)


def count(zmap):
    global cnt, i, j
    cnt += 1
    zmap[0][0] = cnt
    if i == r and j == c:
        return cnt
    
    cnt += 1
    zmap[0][1] = cnt
    j += 1
    if i == r and j == c:
        return cnt
    
    cnt += 1
    zmap[1][0] = cnt
    i += 1
    if i == r and j == c:
        return cnt
    
    cnt += 1
    zmap[1][1] = cnt
    if i == r and j == c:
        return cnt
    
    if j < 3:
        i -= 1
        j += 1
    else:
        i += 1
        j = 0
    return cnt

i,j = 0,0
split(ZMAP)
print(cnt)