# 두 개 뽑아서 더하기
from itertools import combinations

def solution(numbers):
    answer = []
    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            sum = numbers[i] + numbers[j]
            answer.append(sum)

    answer = list(set(answer))

    answer.sort()
    return answer


# 콤비네이션 풀이
def solution2(numbers):
    answer = []
    l = list(combinations(numbers, 2))

    for i in l:
        answer.append(i[0] + i[1])
    answer = list(set(answer))
    answer.sort()


print(solution([5, 0, 2, 7]))
