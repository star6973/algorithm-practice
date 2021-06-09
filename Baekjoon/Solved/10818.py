N = int(input())
n = list(map(int, input().split()))

min_num = 1000000
max_num = -1000000

for i in range(len(n)):
    if min_num >= n[i]:
        min_num = n[i]
    if max_num <= n[i]:
        max_num = n[i]

print(min_num, max_num)