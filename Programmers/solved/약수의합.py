def solution(n):
    answer = 0
    measure = []
    for i in range(1, n+1):
        if n % i == 0:
            measure.append(i)
    answer = sum(measure)

    return answer

n = 5
s = solution(n)
print(s)