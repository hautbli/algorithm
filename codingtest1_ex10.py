# 2016년
from datetime import date


def solution(a, b):
    answer = ''
    day = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    return day[date(2016, a, b).weekday()]


print(solution(5, 24))
