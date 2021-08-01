def solution(n):
    answer = 0

    ternary = []
    div = -1
    while div != 0:
        div = n // 3
        ternary.append(n % 3)
        n = div

    for i in range(len(ternary)):
        answer += ternary[i] * (3**(len(ternary) - i - 1))
    
    return answer

n = 45
s = solution(n)
print(s)