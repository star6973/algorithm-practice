import re

N, K = map(int, input().split())
circle = [i+1 for i in range(N)]
yosepus = []

i = 0
p = 0
while True:

    if len(circle) == 1 and p == 0:
        yosepus.append(circle.pop(i))
        break

    # 인덱스 위치가 K와 같다면, 요세푸스 리스트에 추가 및 K 초기화
    if p == K - 1:
        yosepus.append(circle.pop(i))
        p = 0
    else:
        i += 1
        p += 1

    # 인덱스 위치가 현재 circle 리스트의 길이를 벗어나면 0으로 초기화
    if i == len(circle):
        i = 0

yosepus = str(yosepus)
yosepus = yosepus.replace('[', '<')
yosepus = yosepus.replace(']', '>')
print(yosepus)