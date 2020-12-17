# h-index (정렬)

def solution(citations):
    citations.sort(reverse=True)
    for i in range(len(citations), 0, -1):
        if i > len(citations) - citations.count(0):
            continue
        if i <= len(list(filter(lambda x: x >= i, citations))):
            return i
    return 0


print(solution([5, 6, 7, 2, 2, 0, 0, 0, 0]))


def solution2(citations):
    citations = sorted(citations)
    l = len(citations)
    for i in range(l):
        if citations[i] >= l - i:
            return l - i
    return 0


print(solution2([5, 6, 7, 2, 2, 0, 0, 0, 0]))
