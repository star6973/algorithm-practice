from collections import deque

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
queue = deque()
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
size = 2
count = {
    0: 0,
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
}
distance = 0

for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[i][j] == 9:
            queue.append([i, j])
            arr[i][j] = 0
            break

while True:
    # 먹을 수 있는 물고기 
    able = []
    for i in range(len(arr)):
        for j in range(len(arr)):
            if 0 < arr[i][j] < size:
                able.append([i, j])

    #
    if len(able) == 0:
        break
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            print("다음 위치 = ", [nx, ny])

            if 0 <= nx < N and 0 <= ny < N:
                # 아기 상어보다 물고기가 더 크면 못 지나감
                if arr[nx][ny] > size:
                    print("넌 못지나간다")
                    continue

                # 아기 상어와 물고기의 크기가 같으면, 지나갈 수는 있지만 못 잡아먹음
                elif arr[nx][ny] == size:
                    print("상어 = 물고기 크기")
                    distance += 1
                    queue.append([nx, ny])

                # 아기 상어가 물고기보다 크면, 잡아먹으면서 지나갈 수 있음
                else:
                    # 0인 위치는 물고기가 없는 위치
                    if arr[nx][ny] == 0:
                        print("조용히 그냥 지나가자")
                        distance += 1
                        queue.append([nx, ny])
                    else:
                        print("잡아먹자")
                        distance += 1
                        count[arr[nx][ny]] += 1

                        # 다음 위치의 물고기 크기가 상어의 크기보다 1 작으면서, 그 크기만큼 상어가 먹었다면, 상어의 크기가 1 증가한다
                        if arr[nx][ny] == size - 1 and count[arr[nx][ny]] == arr[nx][ny]:
                            size += 1

                        queue.append([nx, ny])

    cnt += 1
    print(queue)
    print(arr)

print(size)
print(count)
print(distance)