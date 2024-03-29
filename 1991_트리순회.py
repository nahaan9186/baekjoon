from collections import deque


N = 7

li = [
    ['A', 'B', 'C'],
    ['B', '.', 'D'],
    ['C', 'E', 'F'],
    ['E', '.', '.'],
    ['F', '.', 'G'],
    ['D', '.', '.'],
    ['G', '.', '.']
]
def mk_li(A):
    li = [''.join(item) for item in A]
    return li

#전위 순회
res_preorder = []
def preorder(li,left,right,degree):
    if li[degree][left] is None:
        return -1
    else:
        res_preorder.append(li[degree][left])   # degree가 0일때만 li[0][0] append
        print(f'{res_preorder}, {degree}, {li[degree][left]}')
        if li[degree][left+1] != '.':   # li[0][1] 이 '.'이 아니면 append 후 재귀호출
            if degree == 0:
                res_preorder.append(li[degree][left+1])
                print(f'{res_preorder}, {degree}, {li[degree][left+1]}')
                degree += 1
                preorder(li,left,right,degree)
            else:
                if li[degree][left+1] in res_preorder:
                    degree += 1
                    preorder(li,left,right,degree)
                else:
                    res_preorder.append(li[degree][left+1])
                    print(f'{res_preorder}, {degree}, {li[degree][left+1]}')
                    degree += 1
                    preorder(li,left,right,degree)
        elif li[degree][right] != '.':    # left side append가 다 끝나고, li[0][2] 이 '.'이 아니면 append 후 재귀호출
            if degree == 0:
                res_preorder.append(li[degree][right])
                print(f'{res_preorder}, {degree}, {li[degree][right]}')
                degree += 1
                preorder(li,left,right,degree)
            else:
                if li[degree][right] in res_preorder:
                    degree += 1
                    preorder(li,left,right,degree)
                else:
                    res_preorder.append(li[degree][right])
                    print(f'{res_preorder}, {degree}, {li[degree][right]}')
                    degree += 1
                    preorder(li,left,right,degree)
        return res_preorder

        


#중위 순회
def inorder(li):
    return 0

#후위 순회
def postorder(li):
    return 0

mk_li = mk_li(li)
print(mk_li)

print(f'preorder = {preorder(mk_li,0,2,0)}')

print(f'inorder = {inorder(li)}')

print(f'postorder = {postorder(li)}')
