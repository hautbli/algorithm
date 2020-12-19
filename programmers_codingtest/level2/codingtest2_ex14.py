# 큰 수 만들기 (탐욕법)

def solution(number, k):
    st = []

    # 큰 수가 앞자리가 되게끔 스택에 저장
    for elem in number:
        while st and st[-1] < elem and k > 0:
            st.pop()
            k -= 1

        st.append(elem)

    # k가 남았다면 뒤에서부터 빼기
    while k > 0:
        st.pop()
        k -= 1

    answer = "".join(st)
    return answer


print(solution('1925', 2))
