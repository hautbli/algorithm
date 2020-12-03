# 주식 가격
from collections import deque


def solution(prices):
    # 시간 초과
    prices = deque(prices)
    answer = []
    for _ in range(len(prices)):
        ele = prices.popleft()

        if not prices:
            # prices 가 빈 큐일경우
            # 0을 append하고 return
            answer.append(0)
            return answer
        if min(prices) < ele:
            # 그 ele 보다 작은 원소의 idx 리스트를 만든 후
            # 첫번째의 ele를 answer에 append
            a = get(ele, prices)
            answer.append(a)
        else:
            # 작은게 없을 경우 끝까지 가니까 len append
            answer.append(len(prices))


def get(ele, prices):
    for idx, v in enumerate(prices):
        if v < ele:
            return idx + 1


def solution2(prices):
    answer = []
    prices = deque(prices)
    while prices:
        c = prices.popleft()

        count = 0
        for i in prices:
            if c > i:
                count += 1
                break
            count += 1

        answer.append(count)

    return answer



print(solution([1, 2, 3, 2, 3]) == [4, 3, 1, 1, 0])
print(solution([1, 2, 3, 2, 3]))
