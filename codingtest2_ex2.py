# 문자열 압축
def solution(s):
    answer = len(s)
    for i in range(1, len(s)):
        # i = 쪼개는 단위
        answer_s = ''
        count = 1
        pivot = s[:i]
        for j in range(len(s)): # while 로
            # pivot을 기준으로 중복 개수 찾기
            next_pivot = s[j + i:j + i + i]
            print(pivot, next_pivot)
            if pivot == next_pivot:
                # 중복이 됐을 때는 중복카운트 변수에 + 1
                count += 1
                pivot = s[j+i+i:j + i + i+i]
                print('pivot', pivot)

            else:
                # print(answer_s, i)
                # 피봇이 연속되지 않음
                if 2 <= count:
                    # 2이상 연속되었을 때
                    answer_s += str(count) + pivot
                else:
                    curr = pivot[0]
                    answer_s += curr
                    # print('curr', curr)
                count = 1
                # pivot 체인지
                pivot = s[j + 1:j + 1 + i]
        # print(answer_s, i)
        answer = len(answer_s) if len(answer_s) < answer else answer

    return answer


print(solution('aaabacccccxxx'))
