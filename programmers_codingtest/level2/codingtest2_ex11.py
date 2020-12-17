# 위장 (해시)


def solution(clothes):
    clothes_dict = {}
    for name, kind in clothes:
        if kind not in clothes_dict:
            clothes_dict[kind] = 1
        else:
            clothes_dict[kind] += 1
    answer = 1
    for v in clothes_dict.values():
        # 해당 kind를 제외한 경우를 1로 추가
        answer *= (v + 1)

    return answer - 1


print(solution([['crow_mask', 'face'], ['blue_sunglasses', 'face'], ['smoky_makeup', 'face']]))
