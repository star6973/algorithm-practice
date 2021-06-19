def solution(A):
    A.sort()
    B = [i for i in range(1, len(A)+1)]
    
    if A == B:
        return 1
    else:
        return 0

A = [4, 1, 3, 2]
s = solution(A)
print(s)