N, M = map(int, input().split(" "))

graph = []
for i in range(N):
    graph.append(list(map(int, input())))

from collections import deque

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y)) # deque에 한 번에 초기화하지 말고 append를 이용해서

    while queue:
        x, y = queue.popleft()

        # 상, 하, 좌, 우 모두 방문
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 다음 좌표가 미로의 범위를 벗어난 경우
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            
            # 다음 좌표가 벽인 경우
            if graph[nx][ny] == 0:
                continue
            
            # 다음 좌표가 방문하지 않은 1인 경우
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    # 마지막 칸의 값을 반환
    return graph[N-1][M-1]

print(bfs(0, 0))