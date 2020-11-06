# 서울에서 김서방 찾기

def solution(seoul):
    answer = ''
    idx = seoul.index('Kim')
    answer = f'김서방은 {idx}에 있다'
    return answer

print(solution(['Jane', 'Kim']))