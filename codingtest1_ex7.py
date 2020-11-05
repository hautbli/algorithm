# 3진법 뒤집기
def solution(n):
    tentothree = []
    quo, rem = divmod(n, 3)
    tentothree.append(rem)
    while 0 != quo:
        quo, rem = divmod(quo, 3)
        tentothree.append(rem)

    threetoten = 0
    tentothree.reverse()
    for idx, elem in enumerate(tentothree):
        threetoten += elem * 3 ** idx

    return threetoten


print(solution(1))  # 1200


def solution(n):
    answer = []
    while True:
        if n < 3:
            answer.append(n)
            break
        answer.append(n % 3)
        n = n // 3
    answer.reverse()
    sum = 0
    for i in range(len(answer)):
        sum += (answer[i] * (3 ** i))
    return sum