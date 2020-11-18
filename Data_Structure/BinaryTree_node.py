class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self, array):
        node_list = [Node(value, None, None) for value in array]
        for ind, node in enumerate(node_list):
            left = 2 * ind + 1
            right = 2 * ind + 2

            if left < len(node_list):
                node.left = node_list[left]
            if right < len(node_list):
                node.right = node_list[right]

        self.root = node_list[0]

    def preorder(self):
        def recursive(node):
            nonlocal s
            # 자신 조회
            s += str(node.value) + ' '
            # 레프트 조회
            if node.left:
                recursive(node.left)
            # 라이트 조회
            if node.right:
                recursive(node.right)

        s = '['
        recursive(self.root)
        s += ']'
        print(s)

    def inorder(self):
        def recursive(node):
            nonlocal s
            # left
            if node.left:
                recursive(node.left)
            # node
            s += str(node.value) + ' '
            # right
            if node.right:
                recursive(node.right)

        s = '['
        recursive(self.root)
        s += ']'
        print(s)

    def postorder(self):
        def recursive(node):
            nonlocal s
            # left
            if node.left:
                recursive(node.left)
            # right
            if node.right:
                recursive(node.right)
            # node
            s += str(node.value) + ' '

        s = '['
        recursive(self.root)
        s += ']'
        print(s)

    def bfs(self, value):
        return False

    def dfs(self, value):
        def recursive(node):
            nonlocal found

        return False


tree = BinaryTree([i for i in range(13)])
tree.preorder()
tree.inorder()
tree.postorder()
