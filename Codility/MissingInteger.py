def solution(A):
    A.sort()
    min_num = 1

    for a in A:
        if a == min_num:
            min_num += 1

    return min_num


A = [-1, -2, -3]
s = solution(A)
print(s)