# 큰 수 만들기 (탐욕법)
from itertools import permutations


def solution(numbers):
    answer = 0
    numbers = list(map(str, numbers))
    numbers = list(permutations(numbers, len(numbers)))
    for n in numbers:
        num = int(''.join(n))
        if answer < num:
            answer = num

    return str(answer)


print(solution([3, 30, 34, 5, 9]))
