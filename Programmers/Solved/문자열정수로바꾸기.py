def solution(s):
    answer = 0

    if s[0] in ['+', '-']:
        for i in range(1, len(s)):
            answer += int(s[i]) * 10**(len(s)-i-1)
        if s[0] == '-':
            answer *= -1
    else:
        for i in range(len(s)):
            answer += int(s[i]) * 10**(len(s)-i-1)
    
    return answer

s = "-1234"
s = solution(s)
print(s)