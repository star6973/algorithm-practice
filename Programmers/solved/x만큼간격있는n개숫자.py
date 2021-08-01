def solution(x, n):
    if x > 0:
        answer = [i for i in range(x, x*n+1, x)]
    elif x < 0:
        answer = [i for i in range(x, x*n-1, x)]
    else:
        answer = [0]*n
    
    return answer

x = 0
n = 2
s = solution(x, n)
print(s)