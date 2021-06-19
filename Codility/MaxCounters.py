# def solution(N, A):
#     counter = [0] * N
#     max_num = 0
#     for a in A:
#         # 배열의 범위를 벗어난 값이 카운팅될 경우, 현재 배열에서 가장 큰 값으로 모두 통일
#         if a > N:
#             counter = [max_num] * N
#         else:
#             counter[a-1] += 1
#             max_num = max(max_num, counter[a-1])

#     return counter


def solution(N, A):
    counters = N * [0]
    next_max_counter =  max_counter = 0

    for a in A:
        if a <= N:
            current_counter = counters[a-1] = max(counters[a-1] +1, max_counter+1)
            next_max_counter = max(current_counter, next_max_counter)
        else:
            max_counter = next_max_counter

    return [c if c > max_counter else max_counter for c in counters]

N = 5
A = [3, 4, 4, 6, 1, 4, 4]
s = solution(N, A)
print(s)