def solution(s):
    answer = True
    number = '0123456789'
    
    if len(s) == 4 or len(s) == 6:
        for i in range(len(s)):
            if s[i] not in list(number):
                answer = False
    else:
        answer = False

    return answer
    
s = "1234"
s = solution(s)
print(s)