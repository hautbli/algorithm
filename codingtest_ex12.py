# 문자열 내 마음대로 정렬하기

def solution(strings, n):
    sorted_list = sorted(strings, key=lambda x: (x[n], x))

    return sorted_list



print(solution(['abce', 'abcd', 'cdx'], 2))
