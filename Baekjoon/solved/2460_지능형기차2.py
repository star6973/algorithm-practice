train = []
tot = 0
for i in range(10):
    down, up = map(int, input().split())
    tot += up - down
    train.append(tot)

print(max(train))