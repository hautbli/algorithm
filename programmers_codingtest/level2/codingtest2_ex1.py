# 조이스틱
from string import ascii_uppercase


def solution(name):
    answer = 0
    name = list(name)
    idx = 0
    while (True):
        right_A_count = 1
        left_A_count = 1
        if name[idx] != 'A':
            # idx가 A가 아닌경우
            # 위아래 -> 더 가까운 것
            updown = min(ord(name[idx]) - ord('A'), ord('Z') - ord(name[idx]) + 1)
            answer += updown

        name[idx] = 'A'
        # print(name)
        if name == ['A'] * len(name): break  # A완성되면 종료!

        # 연속된 A의 개수가 방향으로 가야 최소횟수로 이동할 수 있음
        for i in range(1, len(name)):
            if name[idx + i] == 'A':
                right_A_count += 1
            else:
                break

        for i in range(1, len(name)):
            if name[idx - i] == 'A':
                left_A_count += 1
            else:
                break

        if right_A_count > left_A_count:
            # 왼쪽이 A가 아닌게 더 가까울 때
            answer += left_A_count
            idx -= left_A_count
        else:
            # 오른쪽이 A가 아닌게 더 가까울 때나 둘이 같을 때
            answer += right_A_count
            idx += right_A_count
    return answer


print(solution("JDABSAFE"))

'BBAAAAAAAABBBBBBAA'