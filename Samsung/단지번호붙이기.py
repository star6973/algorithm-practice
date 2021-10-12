from collections import deque

N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def bfs(px, py):
    stack = deque()
    stack.append((px, py))
    visited[px][py] = 1
    cnt = 1 # 단지의 개수

    while stack:
        x, y = stack.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                # 방문하지 않으면서 단지가 존재하는 경우, 방문 처리 후 단지를 빈 곳으로 바꿔준다.
                if visited[nx][ny] == 0 and arr[nx][ny] == 1:
                    visited[nx][ny] = 1
                    arr[nx][ny] = 0
                    stack.append((nx, ny))
                    cnt += 1

    return cnt

answer = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            answer.append(bfs(i, j))

answer.sort()
print(len(answer))
for i in range(len(answer)):
    print(answer[i])