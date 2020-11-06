# 나누어떨어지는 숫자배열

def solution(arr, divisor):
    answer = []
    for a in arr:
        if a % divisor == 0:
            answer.append(a)
    if not answer:
        return [-1]
    return sorted(answer)


print(solution([9, 7], 5))

def solution2(arr, divisor):
    arr = [x for x in arr if x % divisor == 0];
    arr.sort();
    return arr if len(arr) != 0 else [-1];