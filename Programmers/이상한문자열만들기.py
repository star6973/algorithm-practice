def solution(s):
    string = s.split(' ')

    # 짝수번째 알파벳은 대문자, 홀수번째 알파벳은 소문자
    answer = []
    for s in string:
        tmp = ''
        for i in range(len(s)):
            if i % 2 == 0:
                tmp += s[i].upper()
            else:
                tmp += s[i].lower()
        answer.append(tmp)

    answer = ' '.join(answer)

    return answer

s = "try hello world"
s = solution(s)
print(s)