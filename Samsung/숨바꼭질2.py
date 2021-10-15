from collections import deque

N, K = map(int, input().split())
MAX_SIZE = 100001

def bfs(n):
    queue = deque([n])

    # check[i][0]: i 위치에 방문했을 때, 걸린 시간
    # check[i][1]: i 위치에 방문했을 때, 걸린 시간의 방법 수
    check = [[-1, 0] for _ in range(MAX_SIZE)]
    check[N][0] = 0
    check[N][1] = 1

    while queue:
        cur_loc = queue.popleft()

        for next_loc in [cur_loc-1, cur_loc+1, cur_loc*2]:
            if 0 <= next_loc < MAX_SIZE:
                # 다음 위치를 방문하지 않은 경우(걸린 시간이 0이라면)
                # 현재 위치 방문 시간에 1을 더해주고, 걸린 시간의 방법의 수를 그대로 유지해준다
                if check[next_loc][0] == -1:
                    check[next_loc][0] = check[cur_loc][0] + 1
                    check[next_loc][1] = check[cur_loc][1]
                    queue.append(next_loc)

                # 다음 위치를 이미 방문한 경우이면서, 1초만큼 차이가 난 경우
                # 현재 위치를 방문하는데 걸린 시간의 방법의 수만큼 더해준다
                elif check[next_loc][0] == check[cur_loc][0] + 1:
                    check[next_loc][1] += check[cur_loc][1]
    
    # 위치 K로 방문했을 때, 걸린 시간과 방법의 수
    return check[K][0], check[K][1]

time, way = bfs(N)
print(time)
print(way)