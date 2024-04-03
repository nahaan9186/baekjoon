import sys
sys.setrecursionlimit(10000)
# li = [50,30,24,5,28,45,98,52,60]
li = []
while True:
    num = sys.stdin.readline().rstrip()
    if num == '':
        break
    else:
        li.append(int(num))

class Node:
    '''node of a binary tree'''
    def __init__(self, root) -> None:
        self.root = root
        self.left = None
        self.right = None

class BinaryTree:
    '''binary tree creation'''
    def __init__(self, li) -> None:
        self.root = None
        for num in li:
            self.root = self.insert(self.root, num)

    def insert(self, node, num):
        '''노드 삽입'''
        if node is None:
            return Node(num)
        else:
            if num < node.root:
                node.left = self.insert(node.left, num)
            else:
                node.right = self.insert(node.right, num)
        return node

    def postorder(self, node, path=[]):
        '''후위 순회'''
        if node:
            self.postorder(node.left, path)
            self.postorder(node.right, path)
            path.append(node.data)
        return path

tree = BinaryTree(li)
path_post = tree.postorder(tree.root, [])
for i in path_post:
    print(i)