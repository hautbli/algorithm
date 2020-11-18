class Node:
    def __init__(self, value, prev, next):
        self.value = value
        self.prev = prev
        self.next = next


class LinkedQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def put(self, value):
        if self.head is None:
            self.head = Node(value, None, None)
            self.tail = self.head
        else:
            node = Node(value, self.tail, None)
            self.tail.next = node
            self.tail = node

    def get(self):
        if self.head is None:
            return None

        value = self.head.value
        if self.head == self.tail:
            # 원소가 하나만 있을 때
            self.head = None
            self.tail = None
            return value

        self.head = self.head.next
        self.head.prev = None
        return value

    def peek(self):
        if self.head is None:
            return False
        else:
            return self.head.value

    def print(self):
        s = '['
        curr = self.head
        while curr is not None:
            s += str(curr.value) + ' '
            curr = curr.next
        s += ']'
        print(s)


queue = LinkedQueue()
queue.print()

queue.put(1)
queue.put(2)
queue.put(3)
queue.put(4)
queue.put(5)
queue.put(6)
queue.print()

print(queue.get())
print(queue.get())
print(queue.get())
print(queue.get())
queue.print()

queue.put(4)
queue.put(5)
queue.put(6)
queue.print()

print(queue.get())
print(queue.get())
print(queue.get())
queue.print()
