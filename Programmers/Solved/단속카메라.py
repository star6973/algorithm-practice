def solution(routes):
    routes = sorted(routes, key=lambda x: x[0])

    flag = -30000
    cnt = 0
    for r in routes:
        if flag < r[0]:
            flag = r[1]
            cnt += 1

        elif flag > r[1]:
            flag = r[1]

    return cnt