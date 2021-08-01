def solution(n):
    answer = 0

    import math
    for i in range(1, int(math.sqrt(n))+1):
        if i**2 == n:
            answer = (i + 1)**2
            break
        else:
            answer = -1
    
    return answer

n = 121
s = solution(n)
print(s)