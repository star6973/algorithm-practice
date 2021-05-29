from collections import defaultdict

N = int(input())
stud = dict()
order = []
for i in range(N*N):
    s = list(map(int, input().split()))
    stud[s[0]] = s[1:]
    order.append(s[0])

# print('학생 순서 = ', order)
# print('좋아하는 학생 = ', stud)

seat = [[0 for i in range(N)] for j in range(N)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

# 맨 처음 학생은 무조건 (N/2, N/2) 위치 등록
seat[int(N/2)][int(N/2)] = order[0]
# print('현재 남아있는 자리 = {}\n'.format(seat))

for i in range(N*N):
    if i == 0:
        continue
    # 현재 학생 순서 선택
    now = order[i]
    # print('선택된 학생 = ', now)
    # 그 학생이 좋아하는 학생들이 누구인지 확인
    like = stud[now]
    # print('이 학생이 좋아하는 학생들 = ', like)
    # 남아있는 자리에 좋아하는 학생들의 위치들을 확인
    like_pos = dict()
    for j in range(N):
        for k in range(N):
            if seat[j][k] in like:
                like_pos[seat[j][k]] = [j, k]
    # print('{0} 학생이 좋아하는 학생들의 위치 = {1}'.format(now, like_pos))
    # 조건 1 -  비어있는 칸 중 좋아하는 학생이 인접한 칸에 가장 많은 칸 선택
    # 인접한 칸 구하기
    near_pos = defaultdict(list)
    for k, v in like_pos.items():
        # 조건식(행렬 범위 벗어나면 x)
        for i in range(4):
            nx = v[0] + dx[i]
            ny = v[1] + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if seat[nx][ny] == 0:
                    near_pos[k].append([nx, ny])
    # print('모든 인접한 칸 = ', near_pos)

    # 인접한 칸에 가장 많은 칸이 있으면 그 칸을 선택
    dup_pos = defaultdict(int)
    for k, v in near_pos.items():
        for value in v:
            dup_pos[tuple(value)] += 1

    max_cnt = 0
    max_idx = 0
    for k, v in dup_pos.items():
        if max_cnt < v:
            max_cnt = v
            max_idx = k

    if max_cnt != 1:
        seat[max_idx[0]][max_idx[1]] = now
    else:
        # 조건 2 - 인접한 칸이 많은 경우 비어있는 칸이 가장 많은 칸 선택
        # 비어있는 칸 구하기
        for k, v in near_pos.items():
            # 인접한 칸이 여러 개인 경우, 다시 한 번 인접해있는 비어있는 칸 선택
            near_near_pos = defaultdict(list)
            for value in v:
                for i in range(4):
                    nx = value[0] + dx[i]
                    ny = value[1] + dy[i]
                    
                    if 0 <= nx < N and 0 <= ny < N:
                        if seat[nx][ny] == 0: # 비어있는 칸의 경우만 선택
                            near_near_pos[tuple(value)].append([nx, ny])
            # print('인접해있는 x2 비어있는 칸들 = ', dict(sorted(near_near_pos.items(), key=lambda x: list(x[0]))))
            near_near_pos = dict(sorted(near_near_pos.items(), key=lambda x: list(x[0])))
            
        # 인접해있는 비어있는 칸이 아무것도 없는 경우, 그 자리가 곧 선택된 학생 자리
        if near_near_pos == defaultdict():
            seat[value[0]][value[1]] = now
        else:
            # 조건 3 - 조건 2를 만족하는 칸도 여러 개인 경우 행과 열이 가장 작은 칸을 선택
            max_len = 0
            max_pos = 0
            for key, value in near_near_pos.items():
                if max_len < len(value):
                    max_len = len(value)
                    max_pos = key
            seat[max_pos[0]][max_pos[1]] = now
    # print('현재 남아있는 자리 = {}\n'.format(seat))

# print("최종 자리 = ", seat)

# 만족도 조사
satisfaction = defaultdict(int)
for i in range(N):
    for j in range(N):
        select_stud = seat[i][j]
        select_stud_like = stud[seat[i][j]]

        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]

            if 0 <= nx < N and 0 <= ny < N:
                if seat[nx][ny] in select_stud_like:
                    satisfaction[select_stud] += 1
 
# print(satisfaction)
result = 0
for k, v in satisfaction.items():
    if v == 0:
        result += 1
    else:
        result += 10**(v-1)
print(result)