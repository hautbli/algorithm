# 조이스틱
from string import ascii_uppercase


def solution(name):
    alpha_list = list(ascii_uppercase)
    answer = 0
    # 위아래
    for ix, n in enumerate(name):
        if n == 'A':
            continue

        idx = alpha_list.index(n)
        _idx = len(alpha_list) - idx

        if idx < _idx:
            answer += idx
        else:
            answer += _idx

    answer += len(name) - 1

    # 근접한 A개수 구하기
    l = 0
    r = 0
    for i in range(1, len(name)):
        if name[i] == 'A':
            l += 1
        else:
            break
    for i in range(1, len(name)):
        if name[-i] == 'A':
            r += 1
        else:
            break
    # l or r
    print(l,r)
    if l < r:
        answer -= r
    else:
        answer -= l
    return answer


print(solution("AAAAAJZA"))
