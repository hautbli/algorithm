# 완주하지 못한 선수
from collections import Counter


def solution(participant, completion):
    participant_dict = dict(Counter(participant))
    completion_dict = dict(Counter(completion))

    for k, v in participant_dict.items():
        try:
            completion_dict[k]
        except:
            return k

        if v != completion_dict[k]:
            return k




def solution2(participant, completion):
    answer = Counter(participant) - Counter(completion)
    return list(answer.keys())[0]


print(solution2(['marina', 'josipa', 'nikola', 'filipa', 'filipa'], ['josipa', 'filipa', 'marina', 'nikola']))
