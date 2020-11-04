# k번째 수

def solution(array, commands):
    answer = []

    for commands_in in commands:
        first = commands_in[0]
        end = commands_in[1]
        return_idx = commands_in[2]

        new_array = array[first - 1:end]
        new_array.sort()
        return_value = new_array[return_idx - 1]
        answer.append(return_value)

    return answer


array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(array, commands))


def solution2(array, commands):
    answer = []
    for command in commands:
        i, j, k = command
        answer.append(list(sorted(array[i - 1:j]))[k - 1])
    return answer


def solution3(array, commands):
    return list(map(lambda x: sorted(array[x[0] - 1:x[1]])[x[2] - 1], commands))
