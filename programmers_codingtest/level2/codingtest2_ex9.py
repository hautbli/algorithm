# 기능 개발 (스택/큐)
from collections import deque


def solution(progresses, speeds):
    answer = []
    day_list = []
    for p, s in zip(progresses, speeds):
        i = 0
        # 100이 될 때까지 s씩 더함
        # 몇 번 더했는지 day_list에 append
        while p + s <= 100:
            i += 1
            p += s
        day_list.append(i + 1)

    day_list = deque(day_list)
    while day_list:
        ele = day_list.popleft()
        count = 0
        # day_list에서 pop을 하고 그 뒤에 요소가 pop한 것보다 작거나 같은지(중요) 체크
        # 작으면 count를 더하고 count 만큼 pop을 한다
        for i in day_list:
            if i <= ele:
                count += 1
            else:
                break

        for i in range(count):
            day_list.popleft()
        answer.append(count + 1)
    return answer


print(solution([93, 30, 55], [1, 30, 5]))
