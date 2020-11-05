# 크레인 인형뽑기 게임

def solution(board, moves):
    answer = 0
    pick_list = []
    # pick list
    for m in moves:
        for ay in board:
            if ay[m - 1] != 0:
                pick_list.append(ay[m - 1])
                ay[m - 1] = 0
                break
    # 연속 원소 제거
    i = 0
    while True:
        if pick_list[i] == pick_list[i + 1]:
            answer += 2
            del pick_list[i]

            del pick_list[i]
            i = 0
        else:
            i += 1
        no = 0
        for a in range(len(pick_list) - 1):
            if pick_list[a] == pick_list[a + 1]:
                no += 1
        if no == 0:
            return answer


print(solution([[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]],
               [1, 5, 3, 5, 1, 2, 1, 4]))


def solution2(board, moves):
    stacklist = []
    answer = 0

    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                stacklist.append(board[j][i-1])
                board[j][i-1] = 0

                if len(stacklist) > 1:
                    if stacklist[-1] == stacklist[-2]:
                        stacklist.pop(-1)
                        stacklist.pop(-1)
                        answer += 2
                break

    return answer