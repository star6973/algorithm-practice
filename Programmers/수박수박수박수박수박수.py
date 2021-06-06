def solution(n):
    answer = ''
    
    if n == 1:
        answer += '수'
    else:
        for i in range(1, n+1):
            if i % 2 != 0:
                answer += '수'
            else:
                answer += '박'
    
    return answer

n = 4
s = solution(n)
print(s)