# value, next, 그리고 prev property를 지닌 Node 클래스를 구현한다.
# Node를 이용하여 Doubly Linked List를 구현한다.
# 다음과 같은 리스트 ADT의 연산자를 구현해야 한다.
# 비어있는 리스트를 생성하는 생성자
# 리스트가 비어있는지 확인하는 연산자
# 리스트의 앞에 개체를 삽입(prepending)하는 연산자
# 리스트의 뒤에 개체를 삽입(appending)하는 연산자
# 리스트의 첫 머리(head)를 결정하는 연산자
# 주어진 인덱스에 해당하는 요소에 접근하는 연산자
# 주어진 인덱스에 새로운 요소를 삽입하는 연산자
# 주어진 인덱스에 해당하는 요소를 제거하는 연산자

class Node:
    def __init__(self, value, next, prev):
        self.value = value
        self.next = next
        self.prev = prev


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def prepend(self, value):
        if self.head is None:
            self.head = Node(value, None, None)
            self.tail = self.head
        else:
            self.head = Node(value, self.head, None)
            self.head.next.prev = self.head

    def append(self, value):
        if self.head is None:
            self.head = Node(value, None, None)
            self.tail = self.head

        else:
            node = Node(value, None, self.tail)
            self.tail.next = node
            self.tail = node

    def set_head(self, index):
        curr = self.head
        for _ in range(index):
            if curr is None:
                return False
            curr = curr.next
        curr.prev = None
        self.head = curr
        return True

    def access(self, index):
        if self.head is None:
            return False
        curr = self.head
        for _ in range(index):
            if curr is None:
                return False
            curr = curr.next
        if curr is None:
            return False
        else:
            return curr.value

    def insert(self, index, value):
        if self.head is None and index > 0:
            return False

        if index == 0:
            self.prepend(value)
            return True

        curr = self.head
        for _ in range(index):
            if curr is None:
                return False
            curr = curr.next

        if curr is None:
            node = Node(value, None, self.tail)
            self.tail.next = node
            self.tail = node
        else:
            curr.prev.next = Node(value, curr, curr.prev)
            curr.prev = curr.prev.next
        return True

    def remove(self, index):
        if self.head is None:
            return False

        if index == 0:
            if self.head is not None:
                self.head = self.head.next
                self.head.prev = None
                return True
            else:
                return False

        curr = self.head
        for _ in range(index):
            if curr is None:
                return False
            curr = curr.next

        if curr is None:
            return False
        else:
            if curr.next is not None:
                curr.prev.next = curr.next
                curr.next.prev = curr.prev

                if curr == self.tail:
                    self.tail = curr.prev
            return True

    def print(self):
        if self.head is None:
            print('[]')
        else:
            curr = self.head
            print('[', end='')
            while curr.next is not None:

                if curr.prev is None:
                    print(curr.value, end=', ')

                elif curr.prev.next == curr.next.prev:
                    print(curr.value, end=', ')
                else:
                    raise ValueError

                curr = curr.next
            print(str(curr.value) + ']')


my_list = DoublyLinkedList()
my_list.print()

for i in range(10):
    my_list.append(i + 1)

my_list.print()

for i in range(10):
    my_list.prepend(i + 1)

my_list.print()

value = my_list.access(3)
print('my_list.access(3) = ' + str(value))

my_list.insert(8, 128)
my_list.print()

my_list.remove(4)
my_list.print()

my_list.set_head(10)
my_list.print()
