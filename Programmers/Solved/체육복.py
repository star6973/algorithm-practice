def solution(n, lost, reserve):
    answer = 0
    cnt_shirts = [1 for _ in range(n)]
    for i in range(1, len(cnt_shirts)+1):
        if i in lost:
            cnt_shirts[i-1] = 0
        if i in reserve:
            cnt_shirts[i-1] += 1

    for i in range(len(cnt_shirts)):
        if cnt_shirts[i] == 0:
            if i-1 >= 0 and cnt_shirts[i-1] >= 2:
                cnt_shirts[i] = 1
                cnt_shirts[i-1] = 1
            elif i+1 < len(cnt_shirts) and cnt_shirts[i+1] >= 2:
                cnt_shirts[i] = 1
                cnt_shirts[i+1] = 1

    for i in range(len(cnt_shirts)):
        if cnt_shirts[i] != 0:
            answer += 1

    return answer

n = 3
lost = [3]
reserve = [1]
s = solution(n, lost, reserve)
print(s)