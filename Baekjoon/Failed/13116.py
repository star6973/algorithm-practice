N = int(input())
for i in range(N):
    A, B = map(int, input().split())
    
    path_A = []
    path_B = []

    # 2로 나눈 몫이 따라온 길
    div = 0
    while div != 1:
        div = A // 2
        path_A.append(A)
        A = div
    path_A.append(A)

    div = 0
    while div != 1:
        div = B // 2
        path_B.append(B)
        B = div
    path_B.append(B)

    # print(path_A, path_B)

    # 리스트 내에서 공통된 값 찾기
    for a in path_A:
        if a in path_B:
            print(a * 10)
            break