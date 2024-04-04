N = 9
paper = ["0 0 0 1 1 1 -1 -1 -1",
        "0 0 0 1 1 1 -1 -1 -1",
        "0 0 0 1 1 1 -1 -1 -1",
        "1 1 1 0 0 0 0 0 0",
        "1 1 1 0 0 0 0 0 0",
        "1 1 1 0 0 0 0 0 0",
        "0 1 -1 0 1 -1 0 1 -1",
        "0 -1 1 0 1 -1 0 1 -1",
        "0 1 -1 1 0 -1 0 1 -1"]
k = [ _.split() for _ in paper ]
print(k)

def find(k):
    pivot = k[0][0]
    for row in k:
        for col in k[row]:
            

    

def split():
    pass

print("-1로 채워진 종이의 개수")
print("0으로 채워진 종이의 개수")
print("1로 채워진 종이의 개수")