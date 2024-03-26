def move_cnt(no:int,x:int,y:int) -> None:
    # 원판 no개를 x기둥에서 y기둥으로 옮김
    if no > 1:
        move_cnt(no -1, x, 6 -x -y)
    global global_cnt
    global_cnt += 1
    if no > 1:
        move_cnt(no -1, 6 -x -y, y)

def move_print(no:int,x:int,y:int) -> None:
    # 원판 no개를 x기둥에서 y기둥으로 옮김
    if no > 1:
        move_print(no -1, x, 6 -x -y)
    print(f'{x} {y}')
    if no > 1:
        move_print(no -1, 6 -x -y, y)

N = int(input()) # 원판의 개수 N

global_cnt = 0

move_cnt(N,1,3)
print(global_cnt)
move_print(N,1,3)
