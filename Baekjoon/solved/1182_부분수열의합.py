# from itertools import combinations

# N, S = map(int, input().split())
# numbers = list(map(int, input().split()))

# case = []
# for i in range(1, len(numbers)+1):
#     case.append(list(combinations(numbers, i)))

# answer = 0
# for c in case:
#     for i in c:
#         if sum(i) == S:
#             answer += 1

# print(answer)

N, S = map(int, input().split())
numbers = list(map(int, input().split()))
answer = 0

def DFS(idx, tot):
    global answer

    # 탈출 조건은 배열의 인덱스 범위가 넘어갈 때
    if idx >= len(numbers):
        return

    tot += numbers[idx]

    if tot == S:
        answer += 1

    DFS(idx + 1, tot - numbers[idx])
    DFS(idx + 1, tot)

DFS(0, 0)
print(answer)