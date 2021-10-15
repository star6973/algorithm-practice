# A, B = map(int, input().split())

# def bfs(num1, num2, cnt):
#     global num_list
#     # B보다 커지면 실패
#     if num1 > num2:
#         return -1
    
#     if num1 == num2:
#         return cnt
    
#     # 2 곱해주기
#     num_list.append(bfs(num1*2, num2, cnt+1))

#     # 1 붙여주기
#     num_list.append(bfs(int(str(num1) + '1'), num2, cnt+1))

# count = 0
# num_list = []
# flag = False
# bfs(A, B, count)
# answer = -1

# for num in num_list:
#     if num == None or num == -1:
#         continue
#     if num > 0:
#         answer = num + 1

# print(answer)

from collections import deque

A, B = map(int, input().split())
answer = -1
count = 1
queue = deque()
queue.append([A, count])

while queue:
    a, c = queue.popleft()

    if a == B:
        answer = c
        break
    
    if a * 2 <= B:
        queue.append([a*2, c+1])

    if int(str(a) + '1') <= B:
        queue.append([int(str(a) + '1'), c+1])

print(answer)