from collections import deque

N = int(input())
for i in range(N):
    M = int(input())
    arr = [list(map(int, input())) for _ in range(M)]
    visited = [[0] * M for _ in range(M)]
    time = [[0] * M for _ in range(M)]

    queue = deque()
    queue.append((0, 0))
    visited[0][0] = 0
    time[0][0] = arr[0][0] # 최소 비용 기록지

    dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]

    while queue:
        x, y = queue.popleft()

        for j in range(4):
            nx = x + dx[j]
            ny = y + dy[j]

            if 0 <= nx < M and 0 <= ny < M:
                # 방문하지 않았으면, 방문처리 후 복귀 시간 계산하고 queue에 넣어준다.
                if visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    time[nx][ny] = time[x][y] + arr[nx][ny]
                    queue.append((nx, ny))
                
                else:
                    # 현재 위치에서 다음 탐색을 비교해봤을 때(방문한 경우), 복귀 시간이 더 적다면 queue에 다시 넣어서 기록해준다.
                    if time[nx][ny] > time[x][y] + arr[nx][ny]:
                        time[nx][ny] = time[x][y] + arr[nx][ny]
                        queue.append((nx, ny))
    
    print('#{0} {1}'.format(i+1, time[M-1][M-1]))