# [카카오 인턴] 키패드 누르기

def solution(numbers, hand):
    answer = ''
    LEFT = 'L'
    RIGHT = 'R'
    numbers_dict = {
        1: (3, 0), 2: (3, 1), 3: (3, 2),
        4: (2, 0), 5: (2, 1), 6: (2, 2),
        7: (1, 0), 8: (1, 1), 9: (1, 2),
        '*': (0, 0), 0: (0, 1), '#': (0, 2)
    }
    curr = {LEFT: numbers_dict['*'], RIGHT: numbers_dict['#']}

    for n in numbers:
        if n in [1, 4, 7]:
            answer += LEFT
            curr[LEFT] = numbers_dict[n]

        elif n in [3, 6, 9]:
            answer += RIGHT
            curr[RIGHT] = numbers_dict[n]

        else:
            num_tup = numbers_dict[n]

            l_dis = get_distance(curr, num_tup, LEFT)
            r_dis = get_distance(curr, num_tup, RIGHT)

            if l_dis < r_dis:
                answer += LEFT
                curr[LEFT] = num_tup
            elif r_dis < l_dis:
                answer += RIGHT
                curr[RIGHT] = num_tup
            elif l_dis == r_dis:
                if hand == 'right':
                    answer += RIGHT
                    curr[RIGHT] = num_tup
                else:
                    answer += LEFT
                    curr[LEFT] = num_tup

    return answer


def get_distance(curr, num_tup, L_OR_R):
    return abs(num_tup[0] - curr[L_OR_R][0]) + abs(num_tup[1] - curr[L_OR_R][1])


print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], 'left'))
