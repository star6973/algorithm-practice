def solution(seoul):
    answer = ''
    for i, s in enumerate(seoul):
        if s == 'Kim':
            answer = '김서방은 ' + str(i) + '에 있다'

    return answer

seoul = ["Jane", "Kim"]
s = solution(seoul)
print(s)