# 더 맵게 (heap)
import heapq


def solution(scoville, K):
    FAIL = -1
    MINIMUM = 0

    # K이상 절대 될 수 없는 경우
    if len(scoville) == 0 or max(scoville) == 0:
        return FAIL
    heapq.heapify(scoville)
    count = 0

    while True:
        # K 이상이 될 수 없는 경우
        if len(scoville) == 1 and scoville[MINIMUM] < K:
            return FAIL
        if scoville[MINIMUM] >= K:
            return count

        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        mix = first + second * 2

        heapq.heappush(scoville, mix)
        count += 1


print(solution([1, 2, 3, 9, 10, 12], 7))
