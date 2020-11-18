import array


class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.front = 0
        self.rear = 0
        self.array = array.array('l', [0] * capacity)
        self.is_full = False  # 추가!

    def put(self, value):
        # 큐 오버플로우
        if self.is_full:
            print('overflow')
            return False

        # put
        self.array[self.rear] = value
        self.rear = (self.rear + 1) % self.capacity

        if self.rear == self.front:
            self.is_full = True
        return True

    def get(self):
        if self.is_full is False and self.front == self.rear:
            # ['']인 경우
            return None
        self.is_full = False

        value = self.array[self.front]
        self.front = (self.front + 1) % self.capacity
        return value

    def peek(self):
        if self.is_full is False and self.front == self.rear:
            # ['']인 경우
            return None
        return self.array[self.front]

    def print(self):
        if self.is_full is False and self.front == self.rear:
            # ['']인 경우
            print('[]')
        start = self.front
        end = self.rear
        if self.rear <= self.front:
            end += self.capacity

        s = '['
        for i in range(start, end):
            s += str(self.array[i % self.capacity]) + ' '
        s += ']'
        print(s)


queue = CircularQueue(5)
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
