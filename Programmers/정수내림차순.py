def solution(n):
    answer = 0
    n = str(n)
    n = sorted(n, reverse=True)
    answer = int(''.join(n))

    return answer

n = 118372
s = solution(n)
print(s)