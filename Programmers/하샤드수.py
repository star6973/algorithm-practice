def solution(x):
    answer = True
    hashard = list(str(x))
    hashard_sum = 0
    for h in hashard:
        hashard_sum += int(h)

    if x % hashard_sum == 0:
        answer = True
    else:
        answer = False

    return answer

x = 11
s = solution(x)
print(s)