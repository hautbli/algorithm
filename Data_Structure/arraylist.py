# 구현 조건
# class와 array.array를 이용하여 Array List를 구현한다.
# 데이터의 타입은 l(signed long)으로 한다.
# array.array 객체의 메소드는 아래 메소드만을 사용한다.
# arr[ind](인덱스로 접근), arr[ind:](슬라이싱)
# array.array의 용량(capacity)은 고정되어 있다고 가정한다.
# 배열의 크기가 부족할 때 마다 2배 길이의 array.array를 새로 생성한다.
# 다음과 같은 리스트 ADT의 연산자를 구현해야 한다.
# 비어있는 리스트를 생성하는 생성자
# 리스트가 비어있는지 확인하는 연산자
# 리스트의 앞에 개체를 삽입(prepending)하는 연산자
# 리스트의 뒤에 개체를 삽입(appending)하는 연산자
# 리스트의 첫 머리(head)를 결정하는 연산자
# 주어진 인덱스에 해당하는 요소에 접근하는 연산자
# 주어진 인덱스에 새로운 요소를 삽입하는 연산자
# 주어진 인덱스에 해당하는 요소를 제거하는 연산자
import array


class ArrayList:
    def __init__(self, capacity):
        self.capacity = capacity
        self.length = 0
        self.array = array.array('l', [0] * capacity)

    def is_empty(self):
        return self.capacity == 0

    def prepend(self, value):
        if self.capacity == self.length:
            self.capacity *= 2
            new_array = array.array('l', [0] * self.capacity)
            for i in range(self.length):
                new_array[i + 1] = self.array[i]
            self.array = new_array
        else:
            for i in range(self.length - 1, -1, -1):
                self.array[i + 1] = self.array[i]

        self.array[0] = value
        self.length += 1

    def append(self, value):
        if self.capacity == self.length:
            self.capacity *= 2
            new_array = array.array('l', [0] * self.capacity)
            for i in range(self.length):
                new_array[i] = self.array[i]
            self.array = new_array

        self.array[self.length] = value
        self.length += 1

    def set_head(self, index):
        self.array = self.array[index:]
        self.capacity = self.capacity - index
        self.length = self.length - index

    def access(self, index):
        return self.array[index]

    def insert(self, index, value):
        if self.capacity == self.length:
            self.capacity *= 2
            new_array = array.array('l', [0] * self.capacity)
            for i in range(index, self.length):
                new_array[i] = self.array[i]
            self.array = new_array
        else:
            for i in range(self.length - 1, index - 1, -1):
                self.array[i + 1] = self.array[i]

        self.array[index] = value
        self.length += 1

    def remove(self, index):
        for i in range(index, self.length - 1):
            self.array[i] = self.array[i + 1]
        self.length -= 1

    def print(self):
        print(self.array.tolist()[:self.length])


my_list = ArrayList(8)
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
