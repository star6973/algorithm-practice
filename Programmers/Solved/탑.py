# def solution(heights):
#
#     heights = list(reversed(heights))
#     answer = [0 for _ in range(len(heights))]
#     stack = []
#     p = 0
#     for idx, h in enumerate(heights):
#
#         if len(stack) == 0:
#             stack.append(h)
#         elif stack[-1] >= h:
#             stack.append(h)
#             p += 1
#         elif stack[-1] < h:
#             k = p
#             while stack[-1] < h:
#                 stack.pop()
#                 answer[p] = len(heights) - idx
#                 p -= 1
#                 if len(stack) == 0:
#                     p += 1
#                     break
#             p = k + 1
#             stack.append(h)
#
#     return list(reversed(answer))

def solution(h):
    ans = [0] * len(h)
    for i in range(len(h)-1, 0, -1):
        for j in range(i-1, -1, -1):
            if h[i] < h[j]:
                ans[i] = j+1
                break
    return ans


print(solution([3,9,9,3,5,7,2]))