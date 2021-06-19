def solution(A):
    li = [0] * (len(A) + 1)
    for i in A:
        li[i-1] = 1
    return li.index(0) + 1

A = [1, 2, 3, 5]
s = solution(A)
print(s)