def solution(X, Y, D):
    Y -= X
    if Y % D == 0:
        return Y // D
    else:
        return Y // D + 1

X = 3
Y = 999111321
D = 7
s = solution(X, Y, D)
print(s)