cal = int(input())
car = list(map(int, input().split()))

cnt = 0
for i in range(len(car)):
    if cal == car[i]:
        cnt += 1

print(cnt)