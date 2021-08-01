N = int(input())

num = N
div = 0
c = 0
while num != 0:
    div = num // 10
    num = div
    c += 1

result = 0
for i in range(c):
    if i == c - 1:
        result += (N - 10**i + 1) * (i+1)
    else:
        result += (9 * (10**i)) * (i+1)
print(result)