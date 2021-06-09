from collections import defaultdict

N = int(input())
p = [0 for _ in range(N)]
for i in range(N):
    dice = list(map(int, input().split()))
    cnt_dice = defaultdict(int)
    for d in dice:
        cnt_dice[d] += 1
    cnt_dice = dict(sorted(cnt_dice.items(), key=lambda x: x[0]))
    # print(cnt_dice)

    # 같은 눈이 4개가 나오는 경우
    if len(cnt_dice) == 1:
        for k, v in cnt_dice.items():
            p[i] += (50000 + k * 5000)

    if len(cnt_dice) == 2:
        for k, v in cnt_dice.items():
            # 같은 눈이 3개가 나오는 경우
            if v == 3:
                p[i] += (10000 + k * 1000)
                break

            # 같은 눈이 2개가 두 쌍으로 나오는 경우
            if v == 2:
                p[i] += (1000 + k * 500)

    # 같은 눈이 2개가 나오는 경우
    if len(cnt_dice) == 3:
        for k, v in cnt_dice.items():
            if v == 2:
                p[i] += (1000 + k * 100)
                break

    # 서로 다른 눈이 나오는 경우
    if len(cnt_dice) == 4:
        max_num = 0
        for k, v in cnt_dice.items():
            if max_num < k:
                max_num = k
        p[i] += (max_num * 100)

print(max(p))