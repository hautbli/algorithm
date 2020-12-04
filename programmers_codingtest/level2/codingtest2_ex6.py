# 전화번호 목록 (해시)
# set로 먼저 만들어놓은 후 in 으로 체크를 하면 sort를 안해도 됨! -> 1과 2의 차이
# solution1 : 빈리스트에서 1234부터 추가할 경우 뒤에 123이 오면 in 으로 체크가 안됨
# 그래서 sort를 써서 len순서대로 정렬하여 123을 먼저 append하고 1234를 슬라이싱하여 in으로 체크

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
