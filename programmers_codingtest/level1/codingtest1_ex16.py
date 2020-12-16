# 행렬의 덧셈

def solution(arr1, arr2):
    answer = []

    for ar1, ar2 in zip(arr1, arr2):
        line = []
        for a1, a2 in zip(ar1, ar2):
            line.append(a1 + a2)
        answer.append(line)
    return answer


print(solution([[1, 2], [2, 3]], [[3, 4], [5, 6]]))


import numpy as np


def sumMatrix(A, B):
    A = np.array(A)
    B = np.array(B)
    answer = A + B
    return answer.tolist()


print(sumMatrix([[1, 2], [2, 3]], [[3, 4], [5, 6]]))