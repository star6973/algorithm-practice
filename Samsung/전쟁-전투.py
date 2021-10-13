from collections import deque

# 가로 = N, 세로 = M 이다.!!!!
N, M = map(int, input().split())
war = [list(map(str, input())) for _ in range(M)]
visited = [[0] * N for _ in range(M)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
queue = deque()

def bfs(px, py, warrior):
    queue.append([px, py])
    visited[px][py] = 1
    cnt = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < M and 0 <= ny < N:
                if visited[nx][ny] == 0 and war[nx][ny] == warrior:
                    visited[nx][ny] = 1
                    war[nx][ny] = 'Z' # 방문한 곳은 더이상 탐색하지 않도록
                    queue.append([nx, ny])
                    cnt += 1

    return cnt

blue_warrior = []
for x in range(M):
    for y in range(N):
        if war[x][y] == 'B':            
            blue_warrior.append(bfs(x, y, 'B'))

white_warrior = []
for x in range(M):
    for y in range(N):
        if war[x][y] == 'W':
            white_warrior.append(bfs(x, y, 'W'))

blue_warrior_sum = sum([pow(bw, 2) for bw in blue_warrior])
white_warrior_sum = sum([pow(ww, 2) for ww in white_warrior])

print(white_warrior_sum, blue_warrior_sum)