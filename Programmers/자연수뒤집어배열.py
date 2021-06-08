def solution(n):
    n = list(str(n))
    answer = [int(n[i]) for i in range(len(n)-1, -1, -1)]
    return answer

n = 123456810
s = solution(n)
print(s)