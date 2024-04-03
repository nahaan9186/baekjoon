import sys
# N = 7
# li = f'A B C\nB D .\nC E F\nE . .\nF . G\nD . .\nG . .'
N = int (input())
li = [sys.stdin.readline().rstrip() for i in range(N)]
# print(li)
root = li[0][0]

class Node:
    '''node of a binary tree'''
    def __init__(self, data) -> None:
        parts = data.split()
        # print(parts)
        self.node_name = parts[0]
        self.node_left = parts[1] if parts[1] != '.' else None
        self.node_right = parts[2] if parts[2] != '.' else None

class BinaryTree:
    '''binary tree creation'''
    def __init__(self, data_list, root) -> None:
        self.nodes = {}
        for i, data in enumerate(data_list):
            node = Node(data)
            self.nodes[node.node_name] = node

    def preorder(self, root, path):
        '''전위 순회'''
        path.append(root)
        
        left_child = self.nodes[root].node_left
        if left_child != None:
            self.preorder(left_child, path)
        
        right_child = self.nodes[root].node_right
        if right_child != None:
            self.preorder(right_child, path)
        
        return path

    def inorder(self, root, path=[]):
        '''중위 순회'''

        left_child = self.nodes[root].node_left
        if left_child != None:
            self.inorder(left_child, path) 
    
        path.append(root)

        right_child = self.nodes[root].node_right
        if right_child != None:
            self.inorder(right_child, path)     

        return path

    def postorder(self, root, path=[]):
        '''후위 순회'''

        left_child = self.nodes[root].node_left
        if left_child != None:
            self.postorder(left_child, path) 

        right_child = self.nodes[root].node_right
        if right_child != None:
            self.postorder(right_child, path)  

        path.append(root) 

        return path

tree = BinaryTree(li, root)

path_pre = tree.preorder(root,[])
print(''.join(path_pre))
path_in = tree.inorder(root,[])
print(''.join(path_in))
path_post = tree.postorder(root,[])
print(''.join(path_post))