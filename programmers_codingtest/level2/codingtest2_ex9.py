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


# print(solution([93, 30, 55], [1, 30, 5]))


def solution(progresses, speeds):
    answer = []
    time = 0
    count = 0
    while len(progresses) > 0:
        if (progresses[0] + time * speeds[0]) >= 100:
            # 100이 넘었을 경우
            # pop을 하고 count +1
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        else:
            # time은 계속 1씩 더해짐 근데 더해도 100보다 작을 경우
            # 그 전까지의 count는 append
            if count > 0:
                answer.append(count)
                count = 0
            time += 1
    answer.append(count)
    return answer


print(solution([93, 30, 55], [1, 30, 5]))
