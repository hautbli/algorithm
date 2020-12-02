# 프린터
from collections import deque


def solution(priorities, location):
    queue = deque(priorities)
    count = 0
    while queue:
        ele = queue.popleft()
        # location 요소가 이번에 pop 될 요소인지
        if not queue:
            return len(priorities)

        if ele < max(queue):
            queue.append(ele)
            if location == 0:
                location = len(queue) - 1
            else:
                location -= 1
        else:
            # pop
            count += 1
            if location == 0:
                return count
            location -= 1


# 몇 번 째로 출력하는지
print(solution([1, 1, 9, 1, 1, 1], 0) == 5)  # 4 3 2 2 1 -> 4


def solution(priorities, location):
    queue = [(i, p) for i, p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer
