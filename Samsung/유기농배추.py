from collections import deque

def main():
    t = int(input())
    for _ in range(t):
        m, n, k = map(int, input().split())
        arr = [[0] * m for _ in range(n)]
        visited = [[0] * m for _ in range(n)]

        for _ in range(k):
            x, y = map(int, input().split())
            arr[y][x] = 1

        answer = []
        for y in range(n):
            for x in range(m):
                if arr[y][x] == 1:
                    answer.append(bfs(y, x, m, n, arr, visited))

        print(len(answer))

def bfs(iy, ix, m, n, arr, visited):
    queue = deque()
    queue.append([iy, ix])
    visited[iy][ix] = 1
    dy, dx = [0, 0, 1, -1], [-1, 1, 0, 0]
    count = 1 # 이미 처음 위치는 1이므로 카운트가 1인 상태로 시작

    while queue:
        y, x = queue.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < n and 0 <= nx < m:
                if visited[ny][nx] == 0 and arr[ny][nx] == 1:
                    count += 1
                    arr[ny][nx] = 0
                    visited[ny][nx] = 1
                    queue.append([ny, nx])

    return count

if __name__ == "__main__":
    main()