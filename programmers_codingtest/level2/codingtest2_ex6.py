# 전화번호 목록 (해시)
def solution(phone_book):
    phones = []
    phone_book.sort(key=lambda x: len(x))
    for num in phone_book:
        for i in range(len(num)):
            p = num[:i + 1]
            if p in phones:
                return False
        phones.append(num)
    return True


print(solution(['1234', '567', '88', '3434', '123']))
