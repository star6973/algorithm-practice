def isPrime(n):
    cnt = 0
    for i in range(1, n+1):
        if n % i == 0:
            cnt += 1

    if cnt == 2:
        return True
    else:
        return False

M = int(input())
N = int(input())

ans = []
for num in range(M, N+1):
    if isPrime(num):
        ans.append(num)

if len(ans) == 0:
    print(-1)
else:
    print(sum(ans))
    print(min(ans))