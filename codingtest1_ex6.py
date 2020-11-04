# 체육복

def solution(n, lost, reserve):
    commons = set(lost).intersection(reserve)
    lost = list(set(lost)-commons)
    reserve = list(set(reserve)-commons)
    answer = n - len(lost)

    for l in lost:
        if l - 1 in reserve:
            answer += 1
            reserve.remove(l - 1)
        elif l + 1 in reserve:
            answer += 1
            reserve.remove(l + 1)

    return answer


print(solution(5, [1, 4, 5, 6], [2, 4, 5]))
