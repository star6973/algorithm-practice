A, B = map(int, input().split())

i = 1
ans = 0
k = 1
cnt = 0
while True:
    if cnt == k:
        k = k + 1
        cnt = 0

    if A <= i <= B:
        ans += k
    
    if i == B:
        break

    i += 1
    cnt += 1

print(ans)