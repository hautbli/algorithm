# 구명보트
def solution(people, limit):
    answer = 0
    people.sort()
    front = 0
    back = len(people) - 1

    while front <= back:
        answer += 1
        if people[front] + people[back] <= limit:
            front += 1

        back -= 1
    return answer


print(solution([40,50,60,70,80], 100))
