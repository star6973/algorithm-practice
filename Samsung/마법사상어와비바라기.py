n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

move = []
for _ in range(m):
    d, s = map(int, input().split())
    move.append([d, s])

clouds = [[n-1, 0], [n-1, 1], [n-2, 0], [n-2, 1]]

# 8 방향
# 대각선 방향은 1, 3, 5, 7 위치
dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

for i in range(len(move)):
    d, s = move[i][0], move[i][1]

    # 이동
    new_cloud = []
    for j in range(len(clouds)):
        x = clouds[j][0]
        y = clouds[j][1]

        nx = (x + dx[d-1] * s) % n
        ny = (y + dy[d-1] * s) % n

        if nx < 0:
            nx += n
        if ny < 0:
            ny += n

        new_cloud.append([nx, ny])

    visited = [[False] * n for _ in range(n)]
    for nc in new_cloud:
        x, y = nc[0], nc[1]
        arr[x][y] += 1
        visited[x][y] = 1

    # 대각선 방향으로 거리가 1인 칸에서 물이 있는 바구니 수 만큼 증가
    for j in range(len(new_cloud)):
        x, y = new_cloud[j][0], new_cloud[j][1]
        count = 0

        for k in [1, 3, 5, 7]:
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] > 0:
                count += 1

        arr[x][y] += count

    # 구름이 있었던 위치를 제외한 나머지 칸 중 물의 양이 2이상인 칸에 구름 생성
    clouds = []
    for x in range(len(arr)):
        for y in range(len(arr)):
            if not visited[x][y] and arr[x][y] >= 2:
                clouds.append([x, y])
                arr[x][y] -= 2

answer = 0
for i in range(len(arr)):
    for j in range(len(arr)):
        answer += arr[i][j]

print(answer)