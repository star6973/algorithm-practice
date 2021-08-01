def solution(n):
    answer = 0
    n = str(n)
    for i in n:
        answer += int(i)
        
    return answer

n = 123
s = solution(n)
print(s)