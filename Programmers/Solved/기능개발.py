from collections import defaultdict

def solution(progresses, speeds):
    answer = defaultdict(int)
    success_progresses = [0 for _ in range(len(progresses))]

    i = 0
    for p, s in zip(progresses, speeds):
        cnt = 0
        while p < 100:
            p += s
            cnt += 1
        success_progresses[i] = cnt
        i += 1

    i = 0
    max_cnt = success_progresses[0]
    while success_progresses != []:
        cur_progress = success_progresses.pop(0)

        if max_cnt >= cur_progress:
            answer[i] += 1
        else:
            max_cnt = cur_progress
            i += 1
            answer[i] += 1

    answer = list(answer.values())

    return answer

progresses = [93, 30, 55]
speeds = [1, 30, 5]
s = solution(progresses, speeds)
print(s)