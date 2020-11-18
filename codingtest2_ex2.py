# 문자열 압축
def solution(s):
    answer = len(s)
    for unit in range(1, len(s)):
        count = 1
        new_s = ''
        for pivot_idx in range(0, len(s), unit):
            pivot = s[pivot_idx:pivot_idx + unit]
            next_pivot = s[pivot_idx + unit:pivot_idx + unit + unit]

            if pivot == next_pivot:
                count += 1
            else:
                if 2 <= count:
                    new_s += str(count) + pivot
                else:
                    new_s += pivot
                count = 1

        if len(new_s) < answer:
            answer = len(new_s)
    return answer



print(solution('abcabcabcabcdededededede'))
