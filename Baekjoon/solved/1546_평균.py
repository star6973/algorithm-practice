import sys

N = int(input())
scores = list(map(int, sys.stdin.readline().split()))

M = max(scores)
for i in range(len(scores)):
    scores[i] = (scores[i] / M) * 100

total = sum(scores)
print(total / N)