# 문자열 내 p와 y의개수
def solution(s):
    s = s.upper()
    p = 0
    y = 0
    for i in s:
        if i == 'Y':
            y += 1
        if i == 'P':
            p += 1
    if y == p:
        return True
    else:
        return False


print(solution("pPoooyY"))


def numPY(s):
    return s.lower().count('p') == s.lower().count('y')
