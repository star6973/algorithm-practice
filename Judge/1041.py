'''
    1014. 최소 이동거리 구하기 - 2차원

    수업과 동아리 활동과 과제로 바쁜 한기대 생들은 조별모임을 좀더 효율적으로 하고 싶어 합니다.
    조별 모임을 하기 위해서는 조원이 모두가 모임 장소로 이동을 해야 하는데, 전체가 이동하는 이동 거리의 합을 최소로 하고 싶습니다.

    문제를 간단하게 하기 위해서 우리가 2차원 평면상에 있고 이동은 x축, y축으로만 이동할 수 있다고 제한을 둡니다. 만약 위치가
        (1, 4), (8, 1), (4, 2)
    에 있다고 한다면, (4, 2)의 위치로 모이면 총 이동 거리가 10으로 최소가 됩니다.

    # 입력
        입력의 첫 줄에 조원의 수 N (1 <= N <= 100,000) 이 입력 됩니다.
        두번째 줄부터는 N명의 조원의 위치 x, y ( 0 <= x, y <= 10,000) 가 주어집니다.

    # 출력
        모두 이동하는 최소 이동거리를 구해주세요.
'''

# 중요 개념
# 최소 좌표부터 최대 좌표 사이의 중간 값을 구하면 최소 이동거리를 구할 수 있다.
N = int(input())

dis = []
for n in range(N):
    dis.append(list(map(int, input().split())))

if N == 1:
    print(0)
elif N == 2:
    print(abs(dis[0][0] - dis[1][0]) + abs(dis[0][1] - dis[1][1]))
else:
    x_dis = []
    y_dis = []

    for d in dis:
        x_dis.append(d[0])
        y_dis.append(d[1])

    x_dis = sorted(x_dis)
    y_dis = sorted(y_dis)

    # x와 y의 중간 값
    mid_x = x_dis[len(x_dis)//2]
    mid_y = y_dis[len(y_dis)//2]

    x_sum = 0
    y_sum = 0
    for d in dis:
        x_sum += abs(mid_x-d[0])
        y_sum += abs(mid_y-d[1])

    print(x_sum + y_sum)