# 소수 찾기

def solution(n):
    pn = set(range(2, n + 1))
    for i in range(2, n + 1):
        pn -= set(range(2 * i, n + 1, i))

    return len(pn)


print(solution(5))
