C = int(input())

for c in range(C):
    N, L = map(int, input().split())
    cost = list(map(int, input().split()))
    min_avg = 101

    for i in range(len(cost)):
        for j in range(i+1, len(cost)+1):
            if len(cost[i:j]) >= L:
                avg = sum(cost[i:j]) / len(cost[i:j])
                if min_avg >= avg:
                    min_avg = avg

    print('{:.10f}'.format(min_avg))