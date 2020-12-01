# 큰 수 만들기 (탐욕법)
from itertools import permutations


def solution(numbers):
    answer = ''
    for i in range(len(numbers)):
        first = '0'

        for s in map(str, numbers):
            if int(first) < int(s[0]):
                first = s[0]
        numbers.remove(int(s))
        print(numbers)
        answer += first
    return answer


print(solution([3, 30, 34, 5, 9]))
