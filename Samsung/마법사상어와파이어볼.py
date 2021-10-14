N, M, K = map(int, input().split())
fire_balls = []
for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    fire_balls.append([r, c, m, s, d])

arr = [[[] for _ in range(N)] for _ in range(N)]

# 북, 동북, 동, 동남, 남, 남서, 서, 서북
dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]

for _ in range(K):
    # 모든 파이어볼의 이동
    while fire_balls:
        r, c, m, s, d = fire_balls.pop(0)
        nr = (r + dr[d] * s) % N
        nc = (c + dc[d] * s) % N
        arr[nr][nc].append([m, s, d])

    # 2개 이상의 파이어볼이 있는 칸은 하나로 합친다
    for r in range(N):
        for c in range(N):
            if len(arr[r][c]) >= 2:
                sm, ss, cnt_odd, cnt_even, length = 0, 0, 0, 0, len(arr[r][c])

                while arr[r][c]:
                    m, s, d = arr[r][c].pop(0)
                    sm += m
                    ss += s
                    if d % 2 != 0:
                        cnt_odd += 1
                    else:
                        cnt_even += 1

                # 질량은 (합쳐진 질량의 합) / 5
                # 속도는 (합쳐진 속도의 합) / (합쳐진 파이어볼의 개수)
                # 방향은 모두 홀수 or 모두 짝수이면 [0, 2, 4, 6], 아니면 [1, 3, 5, 7]                
                if cnt_odd == length or cnt_even == length:
                    nd = [0, 2, 4, 6]
                else:
                    nd = [1, 3, 5, 7]

                nm = sm // 5
                if nm != 0:
                    ns = ss // length
                    for d in nd:
                        fire_balls.append([r, c, nm, ns, d])

            if len(arr[r][c]) == 1:
                fire_balls.append([r, c] + arr[r][c].pop(0))

# 남아있는 질량의 합
answer = 0
print(sum([balls[2] for balls in fire_balls]))