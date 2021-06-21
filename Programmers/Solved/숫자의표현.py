def solution(n):
    answer = 0

    for i in range(1, n+1):
        tot = 0
        for j in range(i, n+2):
            tot += j
            if tot == n:
                answer += 1
            elif tot > n:
                break

    return answer

n = 15
s = solution(n)
print(s)