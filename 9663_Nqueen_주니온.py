def n_queens(row,col):
    i = len(col) -1
    if (promising(row,col)):
        if (row == i):
            print(col[1:i+1])
        else:
            for _ in range(1,i+1):
                col[row+1] = _
                n_queens(row+1, col) 