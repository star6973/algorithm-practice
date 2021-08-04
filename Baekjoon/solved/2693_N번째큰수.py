T = int(input())
for t in range(T):
    A = list(map(int, input().split()))
    A = sorted(A, reverse=True)
    print(A[2])