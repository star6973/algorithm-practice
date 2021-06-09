def solution(phone_number):
    answer = len(phone_number[:-4])*'*' + phone_number[-4:]
    return answer

phone_number = "8888"
s = solution(phone_number)
print(s) 