class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# 이진 트리 클래스
class BinaryTree:
    def __init__(self):
        self.nodes = {}

    def add_node(self, data, left, right):
        if data not in self.nodes:
            self.nodes[data] = Node(data)
        node = self.nodes[data]

        if left != ".":
            if left not in self.nodes:
                self.nodes[left] = Node(left)
            node.left = self.nodes[left]

        if right != ".":
            if right not in self.nodes:
                self.nodes[right] = Node(right)
            node.right = self.nodes[right]

    def preorder(self, node, path=[]):
        if node:
            path.append(node.data)
            self.preorder(node.left, path)
            self.preorder(node.right, path)
        return path

    def inorder(self, node, path=[]):
        if node:
            self.inorder(node.left, path)
            path.append(node.data)
            self.inorder(node.right, path)
        return path

    def postorder(self, node, path=[]):
        if node:
            self.postorder(node.left, path)
            self.postorder(node.right, path)
            path.append(node.data)
        return path

# 노드 정보 입력
node_info = [
    ("A", "B", "C"),
    ("B", "D", "."),
    ("C", "E", "F"),
    ("E", ".", "."),
    ("F", ".", "G"),
    ("D", ".", "."),
    ("G", ".", ".")
]

# 이진 트리 생성
binary_tree = BinaryTree()
for data, left, right in node_info:
    binary_tree.add_node(data, left, right)

# 순회 결과
preorder_result = binary_tree.preorder(binary_tree.nodes["A"], [])
inorder_result = binary_tree.inorder(binary_tree.nodes["A"], [])
postorder_result = binary_tree.postorder(binary_tree.nodes["A"], [])

preorder_result, inorder_result, postorder_result
