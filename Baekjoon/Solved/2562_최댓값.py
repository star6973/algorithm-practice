import sys

num = [int(sys.stdin.readline().strip()) for _ in range(9)]

max_num = -99999
max_idx = 0
for i in range(len(num)):
    if num[i] >= max_num:
        max_num, max_idx = num[i], i

print(max_num)
print(max_idx + 1)