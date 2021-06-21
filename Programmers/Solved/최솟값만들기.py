def solution(A, B):
    A = sorted(A) # 오름차순 정렬
    B = sorted(B, reverse=True) # 내림차순 정렬

    answer = sum([a * b for a, b in zip(A, B)])

    return answer

A, B = [1, 4, 2], [5, 4, 4]
s = solution(A, B)
print(s)