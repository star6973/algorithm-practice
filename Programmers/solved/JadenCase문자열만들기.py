def solution(s):
    answer = []

    for i in range(len(s)):
        # 첫 글자이면서 뒤에 공백인 경우
        if i == 0:
            answer.append(s[i].upper())
        # 앞 글자가 공백이면, 현재 글자는 문자의 첫 글자
        elif s[i-1] == " ":
            answer.append(s[i].upper())
        elif s[i] == " ":
            answer.append(" ")
        else:
            answer.append(s[i].lower())

    return ''.join(answer)

string = "1ab"
s = solution(string)
print(s)