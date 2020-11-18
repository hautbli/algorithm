# 모의 고사
from collections import Counter


def solution(answers):
    s1 = [1, 2, 3, 4, 5]  # 5의 배수
    s2 = [2, 1, 2, 3, 2, 4, 2, 5]  # 8의 배수
    s3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]  # 10의 배수

    count = []

    for i in range(len(answers)):
        if s1[i % len(s1)] == answers[i]:
            count.append(1)
        if s2[i % len(s2)] == answers[i]:
            count.append(2)
        if s3[i % len(s3)] == answers[i]:
            count.append(3)

    result = dict(Counter(count))
    max_value = max((result.values()))

    answer = []
    for k, v in result.items():
        if v == max_value:
            answer.append(k)

    return sorted(answer)


print(solution([1, 3, 2, 4, 2]))


def solution2(answers):
    pattern1 = [1, 2, 3, 4, 5]
    pattern2 = [2, 1, 2, 3, 2, 4, 2, 5]
    pattern3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers):
        if answer == pattern1[idx % len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx % len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx % len(pattern3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx + 1)

    return result
