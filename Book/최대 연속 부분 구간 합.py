arr = [-7, 4, -3, 6, 3, -8, 3, 4]

# 1. 주어진 배열의 모든 부분 구간을 순회하면서 그 합을 계산하는 알고리즘
def inefficientMaxSum(A):
    N = len(A)
    ret = -987654321
    for i in range(N):
        for j in range(i, N):
            sum = 0
            for k in range(i, j+1):
                sum += A[k]
            ret = max(ret, sum)
    return ret

print(inefficientMaxSum(arr))

def betterMaxSum(A):
    N = len(A)
    ret = -987654321
    for i in range(N):
        sum = 0
        for j in range(i, N):
            sum += A[j]
            ret = max(ret, sum)
    return ret

print(betterMaxSum(arr))

# # 2. 재귀 호출과 탐욕법을 이용해 계산하는 분할 정복 알고리즘
# def fastMaxSum(A, lo, hi):
#     # 구간의 길이가 1인 경우
#     if lo == hi:
#         return A[lo]
#
#     mid = (lo + hi) // 2
#
#     # 두 부분에 모두 걸쳐있는 최대 합 구간을 찾는다. 이 구간은 A[i..mid]와 A[mid+1..j] 형태를 갖는 구간의 합으로 이루어진다.
#     # A[i..mid] 형태를 갖는 최대 구간을 찾는다.
#     left = -987654321
#     right = -987654321
#     sum = 0
#     for i in range(lo, mid):
#         sum += A[i]
#         left = max(left, sum)
#
#     # A[mid+1..j] 형태를 갖는 최대 구간을 찾는다.
#     sum = 0
#     for j in range(mid, hi):
#         sum += A[j]
#         right = max(right, sum)
#
#     # 최대 구간이 두 조각 중 하나에만 속해있는 경우의 답을 재귀호출로 찾는다.
#     single = max(fastMaxSum(A, lo, mid), fastMaxSum(A, mid, hi))
#
#     # 두 경우 중 최대치를 반환
#     return max(left + right, single)
#
# fastMaxSum(arr, 0, len(arr))

# A[i]를 오른쪽 끝으로 갖는 구간의 최대 합을 반환하는 동적 계획법 알고리즘
def fastestMaxSum(A):
    N = len(A)
    ret = -987654321
    psum = 0
    for i in range(N):
        psum = max(0, psum) + A[i]
        ret = max(psum, ret)
    return ret

print(fastestMaxSum(arr))