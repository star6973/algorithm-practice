def factor(n):
    if n == 1:
        return [1]
    ret = []
    for div in range(2, n):
        print(div)
        # n을 들어온 div값으로 계속 나누어 떨어질 때까지
        while n % div == 0:
            print(n, div, '들어옴')
            n = n // div
            ret.append(div)
            print(ret)
    return ret

print(factor(20))