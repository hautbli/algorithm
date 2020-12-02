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
