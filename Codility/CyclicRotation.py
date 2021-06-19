from collections import deque

def solution(A, K):
    deq = deque(A)

    try:
        for i in range(K):
            tmp = deq.pop()
            deq.insert(0, tmp)

        return list(deq)
    except:
        return []

A = []
K = 1
s = solution(A, K)
print(s)