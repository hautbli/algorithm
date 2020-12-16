# 시저암호

def solution(s, n):
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
