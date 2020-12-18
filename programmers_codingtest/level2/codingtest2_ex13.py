# 카펫 (완전 탐색)


def solution(brown, yellow):
    for height in range(3, brown + 3):
        width = (brown - (height * 2)) // 2 + 2
        y = (width - 2) * (height - 2)
        if yellow == y:
            return [width, height]


print(solution(24, 24))
