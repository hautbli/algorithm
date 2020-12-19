# linked list
import sys

input = sys.stdin.readline


class DList:
    class Node:
        def __init__(self, item, prev, _next):
            self.item = item
            self.prev = prev
            self.next = _next

    def __init__(self):
        self.head = self.Node(None, None, None)
        self.tail = self.Node(None, self.head, None)
        self.head.next = self.tail
        self.cur = self.tail

    def insert(self, p, item):
        t = p.prev
        n = self.Node(item, t, p)
        p.prev = n
        t.next = n

    def delete(self, x):
        f = x.prev
        r = x.next
        f.next = r
        r.prev = f

    def print_list(self):
        p = self.head.next
        while p != self.tail:
            if p.next != self.tail:
                print(p.item, end="")
            else:
                print(p.item)
            p = p.next


s = list(input().rstrip())
dl = DList()
for i in s:
    dl.insert(dl.tail, i)

for _ in range(int(input())):

    command, string = input().split()

    if command == "L":
        if dl.cur.prev.prev is not None:
            dl.cur = dl.cur.prev
    elif command == "D":
        if dl.cur.next is not None:
            dl.cur = dl.cur.next
    elif command == "B":
        if dl.cur.prev.prev is not None:
            dl.delete(dl.cur.prev)
    else:
        dl.insert(dl.cur, string)
dl.print_list()
