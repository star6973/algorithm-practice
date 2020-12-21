'''
    1114. 나무 쌓기 1

    초등학교에 입학한 한기대는 격자 모양의 바닥에 나무 쌓기 놀이를 하고 있습니다.
    정육면체 도형을 격자 모양에 쌓으면서 놀던 기대는 문득 바라보는 방향에 따라서 쌓인 나무의 모양이 달라 보인다는 걸 깨달았습니다.
    쌓인 나무를 위에서 볼때, 오른쪽에서 볼때, 앞쪽에서 볼 때의 개수가 서로 다르다는 걸 깨달은 기대는 그 총 합을 구하고 싶어졌습니다.
    한기대를 도와서 각각의 면에 보이는 나무의 개수의 총합을 구하는 프로그램을 구현해 주세요.
'''

X, Y = map(int, input().split())
block = [[int(x) for x in input().split()] for y in range(Y)]

top = 0
front = 0
side = 0

for y in range(Y):
    for x in range(X):
        if block[y][x] != 0:
            top += 1

for x in range(X):
    max = 0
    for y in range(Y):
        if max < block[y][x]:
            max = block[y][x]
    front += max

for y in range(Y):
    max = 0
    for x in range(X):
        if max < block[y][x]:
            max = block[y][x]
    side += max

print(top+front+side)