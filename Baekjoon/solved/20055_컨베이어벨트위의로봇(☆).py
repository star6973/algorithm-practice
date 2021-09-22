from collections import deque

N, K = map(int, input().split())

#! 로봇의 위치
robot = [0] * (2*N)
robot = deque(robot)

#! 올리는 위치, 내리는 위치
up_idx, down_idx = 0, N-1

#! 내구도
durab = list(map(int, input().split()))
durab = deque(durab)

#! 현재 단계
phase = 1

#! 가장 먼저 올린 로봇의 위치
first_robot = 0

while True:
    #* 1단계 - 로봇과 '함께' 한 칸 회전하기(로봇의 위치와 내구도의 위치 인덱스 한 칸씩 옮기기)
    robot.rotate(1)
    durab.rotate(1)

    #? 내리는 위치에 로봇이 있는가?
    robot[down_idx] = 0

    #* 2단계 - 각 로봇들을 벨트가 회전하는 방향으로 한 칸 이동하기(내구도가 1 이상이 되면)
    curr_idx = down_idx
    while True:
        next_idx = (curr_idx+1) % len(robot)
        
        #* 다음 칸의 내구도가 1 이상이면서, 로봇이 없는 위치라면 이동
        if robot[curr_idx] == 1 and durab[next_idx] >= 1 and robot[next_idx] == 0:
            robot[next_idx], robot[curr_idx] = 1, 0
            durab[next_idx] -= 1

        #* 현재 탐색해야 할 위치 조정
        if curr_idx != 0:
            curr_idx -= 1
        else:
            curr_idx = len(robot)-1

        if curr_idx == first_robot:
            break

    #? 내리는 위치에 로봇이 있는가?
    robot[down_idx] = 0

    #* 3단계 - 올리는 위치에 있는 칸의 내구도가 0이 아니면 로봇을 올린다
    if durab[up_idx] >= 1 and robot[up_idx] == 0:
        robot[up_idx] = 1
        durab[up_idx] -= 1

    #* 4단계 - 내구도가 0인 칸의 개수가 K개 이상이면 과정을 종료하고, 그렇지 않다면 반복한다
    cnt = 0
    for i in range(len(durab)):
        if durab[i] == 0:
            cnt += 1
    
    if cnt >= K:
        print(phase)
        break

    else:
        phase += 1