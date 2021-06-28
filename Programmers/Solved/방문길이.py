from collections import deque

def solution(dirs):
    answer = 0

    start = [0, 0]
    stack = deque()
    i, j = 0, 1
    for dir in dirs:
        if dir == "U" and (j < 5 or j > -5):
            start[j] += 1
        if dir == "D" and (j < 5 or j > -5):
            start[j] -= 1
        if dir == "L" and (i < 5 or i > -5):
            start[i] -= 1
        if dir == "R" and (i < 5 or i > -5):
            start[i] += 1

        print(start)
        stack.append(start)

    print("stack = ", stack)

    return answer

dirs = "ULURRDLLU"
s = solution(dirs)
print(s)