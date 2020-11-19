# 가운데 글자 가져오기
def solution(s):
    answer = ''
    idx = len(s)
    if idx % 2:
        first = int(idx / 2)
        answer = s[first]
    else:
        first = int(idx / 2)
        answer = s[first - 1:first + 1]

    return answer


# s = 'abcde'
s = 'qwer'

print(solution(s))


def string_middle(str):
    leng = len(str)
    if leng % 2 == 0:
        return str[leng // 2 - 1:leng // 2 + 1]
    else:
        return str[leng // 2]
