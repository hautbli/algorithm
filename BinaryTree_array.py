import array
# class와 array.array를 이용하여 완전 이진 트리를 구현한다.
# 데이터는 생성자에서 배열로 입력받는다.
# 다음과 같은 트리의 연산을 구현해야 한다. (자료의 입력과 삭제는 구현하지 않는다.)
# 순회 알고리즘: 순회하는 순서대로 Element를 출력한다.
# 깊이 우선 순회 (Preorder, Depth-First Traversal)
# 대칭 순회 (Inorder, Symmetric Traversal)
# 후위 순회 (Postorder)
# 탐색 알고리즘: 탐색하여 Tree에 해당 value의 존재 여부를 판단한다.
# 넓이 우선 탐색 (Breadth-First Search; BFS)
# 깊이 우선 탐색 (Depth-First Search; DFS)

import array


class BinaryTree:
    def __init__(self, arr):
        self.array = array.array('l', arr)

    def preorder(self):
        def recursive(ind):
            nonlocal s

            left = 2 * ind + 1
            right = 2 * ind + 2

            # 자신 조회
            s += str(self.array[ind]) + ' '

            # Left 자식 조회
            if left < len(self.array):
                print(left, right, 'left')
                recursive(left)

            # Right 자식 조회
            if right < len(self.array):
                print(left, right, 'right')
                recursive(right)

        s = '['
        recursive(0)
        s += ']'
        print(s)

    def inorder(self):
        def recursive(ind):
            nonlocal s
            left = 2 * ind + 1
            right = 2 * ind + 2

            # Left 자식 조회
            if left < len(self.array):
                recursive(left)

            # 자신 조회
            s += str(self.array[ind]) + ' '

            # Right 자식 조회
            if right < len(self.array):
                recursive(right)

        s = '['
        recursive(0)
        s += ']'
        print(s)

    def postorder(self):
        def recursive(ind):
            nonlocal s
            left = 2 * ind + 1
            right = 2 * ind + 2
            if left < len(self.array):
                recursive(left)
            if right < len(self.array):
                recursive(right)
            s += str(self.array[ind]) + ' '

        s = '['
        recursive(0)
        s += ']'
        print(s)

    def bfs(self, value):
        for elem in self.array:
            if elem == value:
                return True
        return False

    def dfs(self, value):
        found = False

        def recursive(ind):
            nonlocal found
            if found is True:
                return

            if self.array[ind] == value:
                found = True
                return

            left = 2 * ind + 1
            right = 2 * ind + 2
            if left < len(self.array):
                recursive(left)
            if right < len(self.array):
                recursive(right)

        recursive(0)
        return found


tree = BinaryTree([i for i in range(1, 11)])
tree.preorder()
tree.inorder()
tree.postorder()

print(tree.dfs(15))
print(tree.dfs(11))

print(tree.bfs(6))
print(tree.bfs(17))


def a(s):
    print(s)


def b(s):
    print(s)


def c(s):
    a(s)
    b(s)


c(1)
