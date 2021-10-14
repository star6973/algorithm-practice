from collections import deque

N, M, K = map(int, input().split())
arr = [[0] * M for _ in range(N)]
visited = [[0] * M for _ in range(N)]
for _ in range(K):
    r, c = map(int, input().split())
    arr[r-1][c-1] = 1

queue = deque()
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def bfs(px, py):
    queue.append([px, py])
    visited[px][py] = 1
    cnt = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if visited[nx][ny] == 0 and arr[nx][ny] == 1:
                    visited[nx][ny] = 1
                    arr[nx][ny] = 0
                    cnt += 1
                    queue.append([nx, ny])
    
    return cnt

answer = []
for x in range(N):
    for y in range(M):
        if arr[x][y] == 1:
            answer.append(bfs(x, y))

print(max(answer))