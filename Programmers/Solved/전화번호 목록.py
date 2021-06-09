'''

    전화번호부에 적힌 전화번호 중, 한 번호가 다른 번호의 접두어인 경우가 있는지 확인하려 합니다.
    전화번호가 다음과 같을 경우, 구조대 전화번호는 영석이의 전화번호의 접두사입니다.

    구조대 : 119
    박준영 : 97 674 223
    지영석 : 11 9552 4421
    전화번호부에 적힌 전화번호를 담은 배열 phone_book 이 solution 함수의 매개변수로 주어질 때,
    어떤 번호가 다른 번호의 접두어인 경우가 있으면 false를 그렇지 않으면 true를 return 하도록 solution 함수를 작성해주세요.

    [제한 조건]
    phone_book의 길이는 1 이상 1,000,000 이하입니다.
    각 전화번호의 길이는 1 이상 20 이하입니다.

'''

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