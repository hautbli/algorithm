def solution_1(n):
    answer = 0
    for i in map(int, list(str(n))):
        answer += i
    return answer
