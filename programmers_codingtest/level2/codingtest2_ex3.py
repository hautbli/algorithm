# 큰 수 만들기 (탐욕법)
from itertools import permutations


def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x * 3, reverse=True)
    print(numbers)

    return str(int(''.join(numbers)))


print(solution([3, 30, 34, 5, 9]))

s = ['28', '4', '8']
s.sort(key=lambda x: x * 3, reverse=True)

# 41, 4   // 441, 414
