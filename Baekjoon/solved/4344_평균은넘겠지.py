import sys

C = int(input())
for i in range(C):
    students = list(map(int, sys.stdin.readline().split()))
    N = students[0]
    students = students[1:]

    mean = sum(students) / N
    cnt = 0
    for s in students:
        if mean < s:
            cnt += 1
    print("{:.3f}%".format(round(cnt / N * 100, 3)))