# 소수 찾기 (완전탐색)
from itertools import permutations


def is_prime(n):
    # 소수이면 True 반환
    if n < 2: return False
    if n in (2, 3): return True
    if n % 2 == 0 or n % 3 == 0: return False
    if n < 9: return True
    k, l = 5, n ** 0.5
    while k <= l:
        if n % k == 0 or n % (k + 2) == 0:
            return False
        k += 6
    return True


def solution(numbers):
    numbers_list = []
    for i in range(1, len(numbers) + 1):
        # 조합을 int(스트링으로 넣으면 011,11이 구분이 안됨) -> 리스트에 추가
        tmp = permutations(numbers, i)
        for n in tmp:
            tmp_int = int(''.join(n))
            numbers_list.append(tmp_int)

    count = 0
    for i in set(numbers_list):  # 조합 중복 제거 -> set
        if is_prime(int(i)):
            count += 1
    return count


print(solution('011'))


def solution2(n):
    a = set()
    for i in range(len(n)):
        a |= set(map(int, map("".join, permutations(list(n), i + 1))))
    a -= set(range(0, 2))  # 0,1 제거
    for i in range(2, int(max(a) ** 0.5) + 1):
        a -= set(range(i * 2, max(a) + 1, i))
    return len(a)


print(solution2('011'))
