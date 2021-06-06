def solution(s):
    answer = True
    s = s.lower()

    cnt = [0, 0]
    for i in range(len(s)):
        if s[i] == 'p':
            cnt[0] += 1
        if s[i] == 'y':
            cnt[1] += 1

    if cnt[0] == cnt[1]:
        answer = True
    else:
        answer = False

    return answer

s = "pPoooyY"
s = solution(s)
print(s)