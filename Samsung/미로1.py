from collections import deque

SIZE = 16

for n in range(10):
    idx = int(input())
    maze = [list(map(int, input())) for _ in range(SIZE)]
    visited = [[0] * SIZE for _ in range(SIZE)]
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    flag = False
    queue = deque()

    start_idx = [0, 0]
    # 시작점 위치 찾기
    for i in range(SIZE):
        for j in range(SIZE):
            if maze[i][j] == 2:
                start_idx = [i, j]
    
    queue.append(start_idx)
    visited[start_idx[0]][start_idx[1]] = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < SIZE and 0 <= ny < SIZE:
                if visited[nx][ny] == 1 or maze[nx][ny] == 1:
                    continue

                if visited[nx][ny] == 0 and maze[nx][ny] == 0:
                    visited[nx][ny] = 1
                    queue.append([nx, ny])

                if visited[nx][ny] == 0 and maze[nx][ny] == 3:
                    flag = True
                    break

    print('#{0} {1}'.format(idx, 1 if flag else 0))