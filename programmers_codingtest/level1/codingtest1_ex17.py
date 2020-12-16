# 시저암호

def solution(s, n):
    # n이 ord(z)를 몇배나 큰 경우는 통과 못 함
    # -> 모듈러 사용!!
    answer = ''
    for i in s:
        if i == ' ':
            answer += ' '
        else:
            if i.islower() and ord('z') < ord(i) + n:
                answer += chr(ord('a') + ord(i) + n - ord('z') - 1)
            elif i.isupper() and ord('Z') < ord(i) + n:
                answer += chr(ord('A') + ord(i) + n - ord('Z') - 1)
            else:
                answer += chr(ord(i) + n)
    return answer


print(solution('a B z', 4))


def solution2(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i] = chr((ord(s[i]) - ord('A') + n) % 26 + ord('A'))
        elif s[i].islower():
            s[i] = chr((ord(s[i]) - ord('a') + n) % 26 + ord('a'))

    return "".join(s)


print(solution2('a B z', 4))
