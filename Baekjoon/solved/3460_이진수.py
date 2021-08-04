T = int(input())
for t in range(T):
    n = int(input())

    bin = []
    while n:
        d = n // 2
        r = n % 2
        bin.append(r)
        n = d

    ans = []
    for i, b in enumerate(bin):
        if b == 1:
            ans.append(str(i))

    print(" ".join(ans))