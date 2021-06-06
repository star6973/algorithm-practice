def solution(a, b):
    answer = 0

    if a > b:
        answer = sum([i for i in range(b, a+1)])
    if a == b:
        answer = a
    if a < b:
        answer = sum([i for i in range(a, b+1)])

    return answer

a = 5
b = 3
s = solution(a, b)
print(s)