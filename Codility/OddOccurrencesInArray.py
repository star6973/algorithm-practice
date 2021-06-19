from collections import defaultdict

def solution(A):
    answer = defaultdict(int)

    for a in A:
        answer[a] += 1

    for k, v in answer.items():
        if v % 2 != 0:
            return k

A = [9, 3]
s = solution(A)
print(s)