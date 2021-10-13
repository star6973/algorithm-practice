# from collections import deque

# N, M = map(int, input().split())
# r, c, d = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(N)]
# visited = [[0] * M for _ in range(N)]
# queue = deque()
# dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1] # 북, 남, 서, 동

# def bfs(px, py, direction):
#     queue.append([px, py])
#     visited[px][py] = 1
#     cnt = 1
#     flag = [0, 0, 0, 0]

#     while queue:
#         x, y = queue.popleft()

#         # 네 방향 모두 청소가 되있거나 벽이라면, 방향 유지 후 후진
#         if flag == [1, 1, 1, 1]:
#             # print("\n현재 위치 = {0} {1}, 현재 방향 = {2}".format(x, y, direction))
#             # print("모든 방향이 청소 되있어서, 후진하기 \n")
#             if direction == 0:
#                 x = x + dx[1]
#                 y = y + dy[1]

#             if direction == 3:
#                 x = x + dx[3]
#                 y = y + dy[3]

#             if direction == 2:
#                 x = x + dx[0]
#                 y = y + dy[0]

#             if direction == 1:
#                 x = x + dx[2]
#                 y = y + dy[2]

#             # 후진하는 곳이 벽이라면, 탈출
#             if arr[x][y] == 1:
#                 break

#             else:
#                 queue.append([x, y])
#                 flag = [0, 0, 0, 0]
#                 continue

#         # 현재 바라보는 방향이 북쪽이면, 탐색해야 할 방향은 서쪽
#         if direction == 0:
#             nx = x + dx[2]
#             ny = y + dy[2]
#             # print('현재 방향은 북쪽, 이동할 방향은 서쪽', nx, ny)

#             # 네 방향 모두 청소가 되있거나 벽이면서, 후진도 되지 않으면 종료
#             if nx < 0 or nx >= N or ny < 0 or ny >= M:
#                 break

#             # 청소하지 않은 공간이 있다면, 방향 회전 및 전진 후 청소
#             if visited[nx][ny] == 0 and arr[nx][ny] == 0:
#                 # print('>>>>>>>>>>>>>>>>>>>> 청소 가능, 서쪽으로 방향 회전')
#                 visited[nx][ny] = 1
#                 queue.append([nx, ny])
#                 cnt += 1
#                 direction = 3
#                 flag[direction] = 0
#                 continue

#             # 청소하지 않은 공간이 없다면, 방향만 회전
#             else:
#                 # print("청소 공간 없음, 서쪽으로 방향만 회전")
#                 direction = 3
#                 queue.append([x, y])
#                 flag[direction] = 1
#                 continue

#         # 현재 바라보는 방향이 서쪽이면, 탐색해야 할 방향은 남쪽
#         if direction == 3:
#             nx = x + dx[1]
#             ny = y + dy[1]
#             # print('현재 방향은 서쪽, 이동할 방향은 남쪽', nx, ny)

#             # 네 방향 모두 청소가 되있거나 벽이면서, 후진도 되지 않으면 종료
#             if nx < 0 or nx >= N or ny < 0 or ny >= M:
#                 break

#             # 청소하지 않은 공간이 있다면, 방향 회전 및 전진 후 청소
#             if visited[nx][ny] == 0 and arr[nx][ny] == 0:
#                 # print('>>>>>>>>>>>>>>>>>>>> 청소 가능, 남쪽으로 방향 회전')
#                 visited[nx][ny] = 1
#                 queue.append([nx, ny])
#                 cnt += 1
#                 direction = 2
#                 flag[direction] = 0
#                 continue

#             # 청소하지 않은 공간이 없다면, 방향만 회전
#             else:
#                 # print("청소 공간 없음, 남쪽으로 방향만 회전")
#                 direction = 2
#                 queue.append([x, y])
#                 flag[direction] = 1
#                 continue

#         # 현재 바라보는 방향이 남쪽이면, 탐색해야 할 방향은 동쪽
#         if direction == 2:
#             nx = x + dx[3]
#             ny = y + dy[3]
#             # print('현재 방향은 남쪽, 이동할 방향은 동쪽', nx, ny)

#             # 네 방향 모두 청소가 되있거나 벽이면서, 후진도 되지 않으면 종료
#             if nx < 0 or nx >= N or ny < 0 or ny >= M:
#                 break

#             # 청소하지 않은 공간이 있다면, 방향 회전 및 전진 후 청소
#             if visited[nx][ny] == 0 and arr[nx][ny] == 0:
#                 # print('>>>>>>>>>>>>>>>>>>>> 청소 가능, 동쪽으로 방향 회전')
#                 visited[nx][ny] = 1
#                 queue.append([nx, ny])
#                 cnt += 1
#                 direction = 1
#                 flag[direction] = 0
#                 continue

#             # 청소하지 않은 공간이 없다면, 방향만 회전
#             else:
#                 # print("청소 공간 없음, 동쪽으로 방향만 회전")
#                 direction = 1
#                 queue.append([x, y])
#                 flag[direction] = 1
#                 continue

#         # 현재 바라보는 방향이 동쪽이면, 탐색해야 할 방향은 북쪽
#         if direction == 1:
#             nx = x + dx[0]
#             ny = y + dy[0]
#             # print('현재 방향은 동쪽, 이동할 방향은 북쪽', nx, ny)

#             # 네 방향 모두 청소가 되있거나 벽이면서, 후진도 되지 않으면 종료
#             if nx < 0 or nx >= N or ny < 0 or ny >= M:
#                 break

#             # 청소하지 않은 공간이 있다면, 방향 회전 및 전진 후 청소
#             if visited[nx][ny] == 0 and arr[nx][ny] == 0:
#                 # print('>>>>>>>>>>>>>>>>>>>> 청소 가능, 북쪽으로 방향 회전')
#                 visited[nx][ny] = 1
#                 queue.append([nx, ny])
#                 cnt += 1
#                 direction = 0
#                 flag[direction] = 0
#                 continue

#             # 청소하지 않은 공간이 없다면, 방향만 회전
#             else:
#                 # print("청소 공간 없음, 북쪽으로 방향만 회전")
#                 direction = 0
#                 queue.append([x, y])
#                 flag[direction] = 1
#                 continue

#     return cnt

# print(bfs(r, c, d))

from collections import deque

N, M = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

queue = deque()
visited = [[0] * M for _ in range(N)]
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1] # 북, 동, 남, 서

queue.append([r, c, d])
visited[r][c] = 1
cnt = 1

while queue:
    print(queue)
    x, y, d = queue.popleft()
    # 움직일 방향(북(0), 동(1), 남(2), 서(3))
    nd = d
    # 움직일 수 있는지
    move = False

    for i in range(4):
        # 현재 위치에서 현재 방향을 기준으로 왼쪽 방향부터 탐색
        nd -= 1
        if nd < 0:
            nd = 3

        # 움직일 방향
        nx = x + dx[nd]
        ny = y + dy[nd]

        if 0 <= nx < N and 0 <= ny < M:
            # 청소를 할 수 있다면
            if visited[nx][ny] == 0 and arr[nx][ny] == 0:
                visited[nx][ny] = 1
                queue.append([nx, ny, nd])
                cnt += 1
                move = True
                break

    # 네 방향 모두 청소되어 있거나 벽인 경우, 바라보는 방향을 유지하면서 후진
    if move == False:
        nx = x - dx[nd]
        ny = y - dy[nd]

        if 0 <= nx < N and 0 <= ny < M:
            if arr[nx][ny] == 0:
                queue.append([nx, ny, nd])

    # 후진조차 안되면, 마지막 queue에 있는 값이 pop되면서 알아서 while문 탈출

print(cnt)