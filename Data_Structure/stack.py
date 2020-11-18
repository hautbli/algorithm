# class와 array.array를 이용하여 스택을 구현한다.
# array.array의 용량(capacity)은 고정되어 있다고 가정한다.
# 배열의 크기가 부족하면 오버플로우가 발생한다.
# 다음과 같은 스택 ADT의 연산자를 구현해야 한다.
# 자료를 Top 위에 삽입하는 연산자 (Push) 더 이상 삽입할 수 없는 경우 오버플로우 발생 (에러 발생)
# 자료를 Top에서 꺼내는 연산자 (Pop) 더 이상 꺼낼 수 없는 경우 언더플로우 발생 (에러 발생)
# Top에 있는 자료를 반환하지만, 삭제하지는 않는 연산자 (Peek)
# 스택이 비어있는지 확인하는 연산자 (Empty)
import array


class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.top = 0
        self.array = array.array('l', [0] * capacity)

    def push(self, value):
        if self.top == self.capacity:
            return False

        self.array[self.top] = value
        self.top += 1
        return True

    def pop(self):
        if self.top == 0:
            return None
        else:
            self.top -= 1
        return self.array[self.top]

    def peek(self):
        if self.top == 0:
            return None
        else:
            return self.array[self.top - 1]

    def print(self):
        print(self.array.tolist()[:self.top])


stack = Stack(4)
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.print()

stack.push(5)
stack.print()

print(stack.pop())
print(stack.pop())
stack.print()

print(stack.peek())
stack.print()

print(stack.pop())
print(stack.pop())
print(stack.pop())
stack.print()
