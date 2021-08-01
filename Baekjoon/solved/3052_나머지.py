import sys

data = [int(sys.stdin.readline().rstrip()) for _ in range(10)]
for i, d in enumerate(data):
    data[i] %= 42

answer = [0 for _ in range(42)]

for d in data:
    answer[d] += 1

result = 0
for i in range(len(answer)):
    if answer[i] > 0:
        result += 1

print(result)