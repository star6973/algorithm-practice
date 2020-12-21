T = int(input())

for t in range(T):
    axis = []
    for n in range(3):
        axis.append(list(map(int, input().split())))

    axis_x = [a[0] for a in axis]
    axis_y = [a[1] for a in axis]

    dup_x = [a for a in axis_x if axis_x.count(a) == 2]
    dup_y = [a for a in axis_y if axis_y.count(a) == 2]

    unique_x = [a for a in axis_x if a not in dup_x][0]
    unique_y = [a for a in axis_y if a not in dup_y][0]
    print(unique_x, unique_y)