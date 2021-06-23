def solution(phoneBook):
    # 정렬을 해주면 앞에서부터 제일 작은 수(1부터 시작)이기 때문에
    # 배열의 다음 숫자가 무조건 같은 경우가 하나 발생할 수 있다. 아닐 경우도 있지만.
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True

phone_book1 = ['119', '97674223', '1195524421']
phone_book2 = ['123', '456', '789']
phone_book3 = ['12', '123', '1235', '567', '88']
phone_book4 = ['12', '345', '1234', '234']

print(solution(phone_book1))
print(solution(phone_book2))
print(solution(phone_book3))
print(solution(phone_book4))