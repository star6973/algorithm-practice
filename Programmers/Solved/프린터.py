from collections import deque

def isThereBig(que, n):
    for q in que:
        k, v = q[0], q[1]
        if n < v:
            return True
    
    return False

def solution(priorities, location):
    answer = []
    queue = deque()
    idx = 0
    for p in priorities:
        queue.append([idx, p])
        idx += 1

    while queue:
        front = queue.popleft()

        if isThereBig(queue, front[1]):
            queue.append(front)
        else:
            answer.append(front)

    for i, ans in enumerate(answer):
        k, v = ans[0], ans[1]
        if k == location:
            return i+1

prior = [1, 1, 9, 1, 1, 1]
loc = 0
s = solution(prior, loc)
print(s)