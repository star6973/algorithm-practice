def solution(A):
    sum1 = 0
    sum2 = sum(A)
    min_diff = 999999999999999

    for p in range(1, len(A)):
        sum1 += A[p-1]
        sum2 -= A[p-1]
        diff = abs(sum1 - sum2)

        if min_diff >= diff:
            min_diff = diff
        
    return min_diff

A = [3, 1, 2, 4, 3]
s = solution(A)
print(s)