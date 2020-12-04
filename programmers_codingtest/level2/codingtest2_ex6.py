# 전화번호 목록 (해시)
# 리스트를 먼저 만들어놓은 후 in으로 체크를 하면 sort를 안해도 됨! -> 1과 2의 차이

def solution1(phone_book):
    phones = []
    phone_book.sort(key=lambda x: len(x))
    for num in phone_book:
        for i in range(len(num)):
            p = num[:i + 1]
            if p in phones:
                return False
        phones.append(num)
    return True


print(solution1(['1234', '567', '88', '3434', '123']))

def solution2(phone_book):
    answer = True
    hash_map = set(phone_book)
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                answer = False
    return answer

print(solution2(['1234', '567', '88', '3434', '123']))
