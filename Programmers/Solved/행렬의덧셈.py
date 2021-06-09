def solution(arr1, arr2):
    answer = [[i + j for i, j in zip(a1, a2)] for a1, a2 in zip(arr1, arr2)]
    return answer

ar1 = [[1],[2]]
ar2 = [[3],[4]]
s = solution(ar1, ar2)
print(s)