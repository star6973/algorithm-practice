from collections import deque

N = int(input())
graph = []
for i in range(N):
    graph.append([int(i) for i in input()])

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[False] * N] * N

def bfs(x, y):
    # 현재 노드는 방문함을 표시
    graph[x][y] = 0
    queue = deque()
    queue.append([x, y])
    cnt = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위 확인해보기
            if nx < 0 or nx >= len(graph) or ny < 0 or ny >= len(graph):
                continue
            
            # 집이 있는 곳인지, 없는 곳인지
            if graph[nx][ny] == 0:
                continue
            
            # 방문한 집이 1 이라면
            if graph[nx][ny] == 1:
                # 현재 노드는 방문함을 표시
                graph[nx][ny] = 0
                queue.append([nx, ny])
                cnt += 1

    if cnt == 0:
        cnt = 1

    return cnt

answer = []
for i in range(len(graph)):
    for j in range(len(graph[i])):
        if graph[i][j] == 1:
            answer.append(bfs(i, j))

answer.sort()
print(len(answer))
for a in answer:
    print(a)