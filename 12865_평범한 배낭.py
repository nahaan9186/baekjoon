def ks(N,K):
    if K-W[N] < 0:
        return ks(N-1, K)
    else:
        return max(ks(N-1, K-W[N])+V[N], 
                  ks(N-1, K))
        
N,K = 4,7
W = [6,4,3,5]
V = [13,8,6,12]